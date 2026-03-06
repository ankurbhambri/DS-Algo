'''
Designing a Movie Ticket Booking System like BookMyShow

Requirements

- The system should allow users to view the list of movies playing in different theaters.
- Users should be able to select a movie, theater, and show timing to book tickets.
- The system should display the seating arrangement of the selected show and allow users to choose seats.
- Users should be able to make payments and confirm their booking.
- The system should handle concurrent bookings and ensure seat availability is updated in real-time.
- The system should support different types of seats (e.g., normal, premium) and pricing.
- The system should allow theater administrators to add, update, and remove movies, shows, and seating arrangements.
- The system should be scalable to handle a large number of concurrent users and bookings.


SOLID Principles applied:
    S - Single Responsibility: MovieService, TheaterService, ShowService, BookingService, PaymentService — each owns one domain.
    O - Open/Closed: PaymentMethod ABC and SeatPricingStrategy ABC — extend with new payment modes or pricing without modifying existing code.
    L - Liskov Substitution: CreditCardPayment, UPIPayment, WalletPayment are all interchangeable via PaymentMethod base.
    I - Interface Segregation: Small focused ABCs (PaymentMethod, SeatPricingStrategy) — no bloated interfaces.
    D - Dependency Inversion: BookingService depends on PaymentMethod abstraction; BookMyShow facade wires services via constructor injection.
'''

import threading
from enum import Enum
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Set


# ======================== Enums ========================

class SeatType(Enum):
    NORMAL = "NORMAL"
    PREMIUM = "PREMIUM"
    VIP = "VIP"


class BookingStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"


class PaymentStatus(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"


# ======================== Models ========================

class Movie:
    def __init__(self, movie_id: str, title: str, language: str, genre: str, duration_min: int):
        self.movie_id = movie_id
        self.title = title
        self.language = language
        self.genre = genre
        self.duration_min = duration_min


class Seat:
    def __init__(self, seat_id: str, row: str, number: int, seat_type: SeatType):
        self.seat_id = seat_id
        self.row = row
        self.number = number
        self.seat_type = seat_type

    def __repr__(self):
        return f"{self.row}{self.number}({self.seat_type.value})"


class Screen:
    def __init__(self, screen_id: str, name: str, seats: List[Seat]):
        self.screen_id = screen_id
        self.name = name
        self.seats = seats


class Theater:
    def __init__(self, theater_id: str, name: str, city: str):
        self.theater_id = theater_id
        self.name = name
        self.city = city
        self.screens: Dict[str, Screen] = {}

    def add_screen(self, screen: Screen):
        self.screens[screen.screen_id] = screen


class Show:
    def __init__(self, show_id: str, movie_id: str, theater_id: str, screen_id: str, start_time: datetime):
        self.show_id = show_id
        self.movie_id = movie_id
        self.theater_id = theater_id
        self.screen_id = screen_id
        self.start_time = start_time
        self._booked_seats: Set[str] = set()
        self._locked_seats: Dict[str, datetime] = {}  # seat_id -> lock_expiry
        self._lock = threading.Lock()

    def get_available_seats(self, screen: Screen) -> List[Seat]:
        """Returns seats that are neither booked nor currently locked."""
        now = datetime.now()
        with self._lock:
            # Clean up expired locks
            expired = [sid for sid, exp in self._locked_seats.items() if exp <= now]
            for sid in expired:
                del self._locked_seats[sid]

            unavailable = self._booked_seats | set(self._locked_seats.keys())
            return [s for s in screen.seats if s.seat_id not in unavailable]

    def lock_seats(self, seat_ids: List[str], timeout_seconds: int = 300) -> bool:
        """Temporarily lock seats during booking flow. Returns False if any seat unavailable."""
        now = datetime.now()
        expiry = now + timedelta(seconds=timeout_seconds)
        with self._lock:
            # Clean up expired locks first
            expired = [sid for sid, exp in self._locked_seats.items() if exp <= now]
            for sid in expired:
                del self._locked_seats[sid]

            for sid in seat_ids:
                if sid in self._booked_seats or sid in self._locked_seats:
                    return False
            for sid in seat_ids:
                self._locked_seats[sid] = expiry
            return True

    def confirm_seats(self, seat_ids: List[str]):
        """Move locked seats to permanently booked."""
        with self._lock:
            for sid in seat_ids:
                self._locked_seats.pop(sid, None)
                self._booked_seats.add(sid)

    def release_seats(self, seat_ids: List[str]):
        """Release locked seats (on cancellation or expiry)."""
        with self._lock:
            for sid in seat_ids:
                self._locked_seats.pop(sid, None)
                self._booked_seats.discard(sid)

    def is_seat_booked(self, seat_id: str) -> bool:
        return seat_id in self._booked_seats


class Booking:
    def __init__(self, booking_id: str, user_id: str, show_id: str, seat_ids: List[str], total_amount: float):
        self.booking_id = booking_id
        self.user_id = user_id
        self.show_id = show_id
        self.seat_ids = seat_ids
        self.total_amount = total_amount
        self.status = BookingStatus.PENDING
        self.payment_status = PaymentStatus.PENDING
        self.timestamp = datetime.now()


class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email


# ======================== Abstractions (OCP + DIP + ISP) ========================

class SeatPricingStrategy(ABC):
    """Open/Closed: add new pricing tiers by subclassing."""
    @abstractmethod
    def get_price(self, seat_type: SeatType) -> float:
        pass


class PaymentMethod(ABC):
    """Interface Segregation: payment is its own focused abstraction."""
    @abstractmethod
    def pay(self, amount: float) -> PaymentStatus:
        pass

    @abstractmethod
    def refund(self, amount: float) -> PaymentStatus:
        pass


# ======================== Strategy Implementations (LSP) ========================

class StandardPricing(SeatPricingStrategy):
    def __init__(self, prices: Optional[Dict[SeatType, float]] = None):
        self._prices = prices or {
            SeatType.NORMAL: 200.0,
            SeatType.PREMIUM: 350.0,
            SeatType.VIP: 500.0,
        }

    def get_price(self, seat_type: SeatType) -> float:
        return self._prices.get(seat_type, 200.0)


class WeekendPricing(SeatPricingStrategy):
    """Weekend surcharge — extend without modifying StandardPricing."""
    def __init__(self, base: SeatPricingStrategy, surcharge_pct: float = 20.0):
        self._base = base
        self._surcharge_pct = surcharge_pct

    def get_price(self, seat_type: SeatType) -> float:
        return self._base.get_price(seat_type) * (1 + self._surcharge_pct / 100)


# ======================== Payment Implementations (LSP) ========================

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float) -> PaymentStatus:
        print(f"  Charged ₹{amount:.2f} to card ending {self.card_number[-4:]}")
        return PaymentStatus.SUCCESS

    def refund(self, amount: float) -> PaymentStatus:
        print(f"  Refunded ₹{amount:.2f} to card ending {self.card_number[-4:]}")
        return PaymentStatus.REFUNDED


class UPIPayment(PaymentMethod):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float) -> PaymentStatus:
        print(f"  Paid ₹{amount:.2f} via UPI {self.upi_id}")
        return PaymentStatus.SUCCESS

    def refund(self, amount: float) -> PaymentStatus:
        print(f"  Refunded ₹{amount:.2f} to UPI {self.upi_id}")
        return PaymentStatus.REFUNDED


class WalletPayment(PaymentMethod):
    def __init__(self, wallet_id: str, balance: float):
        self.wallet_id = wallet_id
        self.balance = balance

    def pay(self, amount: float) -> PaymentStatus:
        if self.balance >= amount:
            self.balance -= amount
            print(f"  Paid ₹{amount:.2f} from wallet. Remaining: ₹{self.balance:.2f}")
            return PaymentStatus.SUCCESS
        print(f"  Wallet has insufficient balance (₹{self.balance:.2f})")
        return PaymentStatus.FAILED

    def refund(self, amount: float) -> PaymentStatus:
        self.balance += amount
        print(f"  Refunded ₹{amount:.2f} to wallet. Balance: ₹{self.balance:.2f}")
        return PaymentStatus.REFUNDED


# ======================== Services (SRP) ========================

class MovieService:
    """SRP: Movie CRUD only."""
    def __init__(self):
        self._movies: Dict[str, Movie] = {}

    def add_movie(self, movie: Movie):
        self._movies[movie.movie_id] = movie

    def get_movie(self, movie_id: str) -> Movie:
        if movie_id not in self._movies:
            raise ValueError(f"Movie {movie_id} not found")
        return self._movies[movie_id]

    def remove_movie(self, movie_id: str):
        if movie_id not in self._movies:
            raise ValueError(f"Movie {movie_id} not found")
        del self._movies[movie_id]

    def list_movies(self) -> List[Movie]:
        return list(self._movies.values())


class TheaterService:
    """SRP: Theater and screen management only."""
    def __init__(self):
        self._theaters: Dict[str, Theater] = {}

    def add_theater(self, theater: Theater):
        self._theaters[theater.theater_id] = theater

    def get_theater(self, theater_id: str) -> Theater:
        if theater_id not in self._theaters:
            raise ValueError(f"Theater {theater_id} not found")
        return self._theaters[theater_id]

    def search_by_city(self, city: str) -> List[Theater]:
        query = city.lower()
        return [t for t in self._theaters.values() if query in t.city.lower()]

    def get_screen(self, theater_id: str, screen_id: str) -> Screen:
        theater = self.get_theater(theater_id)
        if screen_id not in theater.screens:
            raise ValueError(f"Screen {screen_id} not found in theater {theater_id}")
        return theater.screens[screen_id]


class ShowService:
    """SRP: Show scheduling and seat availability."""
    def __init__(self, theater_service: TheaterService):
        self._shows: Dict[str, Show] = {}
        self._theater_service = theater_service

    def add_show(self, show: Show):
        # Validate theater and screen exist
        self._theater_service.get_screen(show.theater_id, show.screen_id)
        self._shows[show.show_id] = show

    def remove_show(self, show_id: str):
        if show_id not in self._shows:
            raise ValueError(f"Show {show_id} not found")
        del self._shows[show_id]

    def get_show(self, show_id: str) -> Show:
        if show_id not in self._shows:
            raise ValueError(f"Show {show_id} not found")
        return self._shows[show_id]

    def get_shows_for_movie(self, movie_id: str) -> List[Show]:
        return [s for s in self._shows.values() if s.movie_id == movie_id]

    def get_shows_for_theater(self, theater_id: str) -> List[Show]:
        return [s for s in self._shows.values() if s.theater_id == theater_id]

    def get_shows_for_movie_in_city(self, movie_id: str, city: str, theater_service: TheaterService) -> List[Show]:
        city_theaters = {t.theater_id for t in theater_service.search_by_city(city)}
        return [s for s in self._shows.values() if s.movie_id == movie_id and s.theater_id in city_theaters]

    def get_available_seats(self, show_id: str) -> List[Seat]:
        show = self.get_show(show_id)
        screen = self._theater_service.get_screen(show.theater_id, show.screen_id)
        return show.get_available_seats(screen)


class BookingService:
    """SRP: Booking creation, confirmation, cancellation.
       DIP: Depends on PaymentMethod abstraction, not concrete classes."""
    def __init__(self, show_service: ShowService, theater_service: TheaterService):
        self._bookings: Dict[str, Booking] = {}
        self._show_service = show_service
        self._theater_service = theater_service
        self._counter = 0

    def create_booking(self, user_id: str, show_id: str, seat_ids: List[str],
                       pricing: SeatPricingStrategy) -> Booking:
        """Lock seats and create a PENDING booking. Must call confirm_booking() to finalize."""
        show = self._show_service.get_show(show_id)
        screen = self._theater_service.get_screen(show.theater_id, show.screen_id)
        seat_map = {s.seat_id: s for s in screen.seats}

        # Validate all requested seats exist
        for sid in seat_ids:
            if sid not in seat_map:
                raise ValueError(f"Seat {sid} does not exist on this screen")

        # Lock seats (concurrent-safe)
        if not show.lock_seats(seat_ids):
            raise ValueError("One or more seats are already booked or locked")

        total = sum(pricing.get_price(seat_map[sid].seat_type) for sid in seat_ids)

        self._counter += 1
        booking = Booking(f"BK{self._counter}", user_id, show_id, seat_ids, total)
        self._bookings[booking.booking_id] = booking
        return booking

    def confirm_booking(self, booking_id: str, payment: PaymentMethod) -> Booking:
        """Process payment and confirm the booking."""
        booking = self._get_booking(booking_id)
        if booking.status != BookingStatus.PENDING:
            raise ValueError(f"Booking {booking_id} is not in PENDING state")

        pay_status = payment.pay(booking.total_amount)
        booking.payment_status = pay_status

        if pay_status == PaymentStatus.SUCCESS:
            show = self._show_service.get_show(booking.show_id)
            show.confirm_seats(booking.seat_ids)
            booking.status = BookingStatus.CONFIRMED
        else:
            # Release seats on payment failure
            show = self._show_service.get_show(booking.show_id)
            show.release_seats(booking.seat_ids)
            booking.status = BookingStatus.CANCELLED

        return booking

    def cancel_booking(self, booking_id: str, payment: PaymentMethod) -> Booking:
        booking = self._get_booking(booking_id)
        if booking.status != BookingStatus.CONFIRMED:
            raise ValueError(f"Only CONFIRMED bookings can be cancelled")

        show = self._show_service.get_show(booking.show_id)
        show.release_seats(booking.seat_ids)

        refund_status = payment.refund(booking.total_amount)
        booking.payment_status = refund_status
        booking.status = BookingStatus.CANCELLED
        return booking

    def get_booking(self, booking_id: str) -> Booking:
        return self._get_booking(booking_id)

    def get_user_bookings(self, user_id: str) -> List[Booking]:
        return [b for b in self._bookings.values() if b.user_id == user_id]

    def _get_booking(self, booking_id: str) -> Booking:
        if booking_id not in self._bookings:
            raise ValueError(f"Booking {booking_id} not found")
        return self._bookings[booking_id]


# ======================== Facade (DIP — depends on service abstractions) ========================

class BookMyShow:
    """Facade that wires all services together for a clean public API."""
    def __init__(self):
        self.movie_service = MovieService()
        self.theater_service = TheaterService()
        self.show_service = ShowService(self.theater_service)
        self.booking_service = BookingService(self.show_service, self.theater_service)


# ======================== Helper to build seats ========================

def create_seats(rows: Dict[str, tuple]) -> List[Seat]:
    """rows = {"A": (10, SeatType.NORMAL), "B": (10, SeatType.NORMAL), "C": (8, SeatType.PREMIUM), ...}"""
    seats = []
    for row, (count, seat_type) in rows.items():
        for i in range(1, count + 1):
            seats.append(Seat(f"{row}{i}", row, i, seat_type))
    return seats


# ======================== Demo ========================

if __name__ == "__main__":

    app = BookMyShow()

    # --- Movies ---
    movies = [
        Movie("M1", "Pushpa 2", "Hindi", "Action", 165),
        Movie("M2", "Inception", "English", "Sci-Fi", 148),
        Movie("M3", "RRR", "Telugu", "Action", 187),
    ]
    for m in movies:
        app.movie_service.add_movie(m)

    print("=== Now Showing ===")
    for m in app.movie_service.list_movies():
        print(f"  {m.title} ({m.language}, {m.genre}, {m.duration_min}min)")

    # --- Theaters & Screens ---
    t1 = Theater("T1", "PVR Saket", "New Delhi")
    screen1_seats = create_seats({"A": (10, SeatType.NORMAL), "B": (10, SeatType.NORMAL),
                                   "C": (8, SeatType.PREMIUM), "D": (6, SeatType.VIP)})
    screen1 = Screen("S1", "Screen 1", screen1_seats)
    t1.add_screen(screen1)
    app.theater_service.add_theater(t1)

    t2 = Theater("T2", "INOX Nariman Point", "Mumbai")
    screen2_seats = create_seats({"A": (12, SeatType.NORMAL), "B": (8, SeatType.PREMIUM)})
    screen2 = Screen("S2", "Audi 1", screen2_seats)
    t2.add_screen(screen2)
    app.theater_service.add_theater(t2)

    # --- Shows ---
    show1 = Show("SH1", "M1", "T1", "S1", datetime(2026, 3, 7, 18, 30))
    show2 = Show("SH2", "M2", "T1", "S1", datetime(2026, 3, 7, 21, 0))
    show3 = Show("SH3", "M1", "T2", "S2", datetime(2026, 3, 7, 19, 0))
    app.show_service.add_show(show1)
    app.show_service.add_show(show2)
    app.show_service.add_show(show3)

    # --- Search: Pushpa 2 in Delhi ---
    print("\n=== Pushpa 2 shows in Delhi ===")
    delhi_shows = app.show_service.get_shows_for_movie_in_city("M1", "delhi", app.theater_service)
    for s in delhi_shows:
        theater = app.theater_service.get_theater(s.theater_id)
        print(f"  {theater.name} — {s.start_time.strftime('%d %b %I:%M %p')}")

    # --- View available seats ---
    print(f"\n=== Available seats for SH1 ===")
    available = app.show_service.get_available_seats("SH1")
    by_type = {}
    for seat in available:
        by_type.setdefault(seat.seat_type.value, []).append(str(seat))
    for stype, seats in by_type.items():
        print(f"  {stype}: {len(seats)} seats — {', '.join(seats[:5])}{'...' if len(seats) > 5 else ''}")

    # --- Booking flow ---
    user = User("U1", "Ankur", "ankur@example.com")
    pricing = StandardPricing()

    print("\n=== Booking 2 PREMIUM + 1 VIP for Pushpa 2 ===")
    booking = app.booking_service.create_booking("U1", "SH1", ["C1", "C2", "D1"], pricing)
    print(f"  Booking {booking.booking_id} created — ₹{booking.total_amount:.2f} — Status: {booking.status.value}")

    # Confirm with UPI
    upi = UPIPayment("ankur@upi")
    confirmed = app.booking_service.confirm_booking(booking.booking_id, upi)
    print(f"  Booking {confirmed.booking_id} — Status: {confirmed.status.value}")

    # --- Verify seats now unavailable ---
    available_after = app.show_service.get_available_seats("SH1")
    print(f"\n  Seats available after booking: {len(available_after)} (was {len(available)})")

    # --- Another user tries same seats (should fail) ---
    print("\n=== Another user tries to book same seats ===")
    try:
        app.booking_service.create_booking("U2", "SH1", ["C1", "D1"], pricing)
    except ValueError as e:
        print(f"  Expected error: {e}")

    # --- Weekend pricing ---
    print("\n=== Weekend pricing example ===")
    weekend = WeekendPricing(StandardPricing(), surcharge_pct=25)
    booking2 = app.booking_service.create_booking("U2", "SH1", ["A1", "A2"], weekend)
    print(f"  Normal weekday: 2 × ₹{pricing.get_price(SeatType.NORMAL)} = ₹{2 * pricing.get_price(SeatType.NORMAL)}")
    print(f"  Weekend price:  ₹{booking2.total_amount:.2f}")
    card = CreditCardPayment("4111111111111234")
    app.booking_service.confirm_booking(booking2.booking_id, card)

    # --- Cancel booking ---
    print(f"\n=== Cancel booking {booking.booking_id} ===")
    app.booking_service.cancel_booking(booking.booking_id, upi)
    print(f"  Status: {booking.status.value}")

    # Seats should be back
    available_after_cancel = app.show_service.get_available_seats("SH1")
    print(f"  Seats available after cancel: {len(available_after_cancel)} (was {len(available_after)})")

    # --- Wallet payment failure ---
    print("\n=== Wallet with insufficient balance ===")
    wallet = WalletPayment("W1", 100.0)
    booking3 = app.booking_service.create_booking("U1", "SH1", ["D2", "D3"], pricing)
    result = app.booking_service.confirm_booking(booking3.booking_id, wallet)
    print(f"  Booking status: {result.status.value} (seats released back)")

    # --- User bookings ---
    print(f"\n=== All bookings for U1 ===")
    for b in app.booking_service.get_user_bookings("U1"):
        print(f"  {b.booking_id} | Show: {b.show_id} | Seats: {b.seat_ids} | "
              f"₹{b.total_amount:.2f} | {b.status.value}")

    # --- Admin: remove a show ---
    print("\n=== Admin removes show SH2 ===")
    app.show_service.remove_show("SH2")
    print(f"  Remaining shows: {[s.show_id for s in app.show_service.get_shows_for_theater('T1')]}")