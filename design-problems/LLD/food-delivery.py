'''
A food delivery system requires the interaction of the restaurants, customers and delivery boys with the admin.

- Restaurants can register themselves.
- Users can create, update, delete, get their profiles.
- Users can search for the restaurant using a restaurant name, city name.
- Restaurants can add, update the food menu.
- Users can see the food menu. Users can get the food items based on Meal type or Cuisine type.
- Users can add/remove items to/from the cart. Users can get all the items of the cart.
- Users can place or cancel the order. Users can get all the orders ordered by them.
- Users can apply the coupons. Users can get the detailed bill containing tax details.
- Users can make a payment using different modes of payment — credit card, wallet, etc.
- Delivery boys can get all the deliveries made by them using their Id.
- Users can get the order status anytime. Success, Out for Delivery, Delivered, etc.


SOLID Principles applied:
    S - Single Responsibility: Each service class has one job (UserService, RestaurantService, CartService, OrderService, etc.)
    O - Open/Closed: PricingStrategy, PaymentMethod, NotificationObserver are open for extension, closed for modification.
    L - Liskov Substitution: All subclasses (CreditCardPayment, WalletPayment, etc.) are interchangeable with their base abstractions.
    I - Interface Segregation: Separate ABCs for PaymentMethod, PricingStrategy, NotificationObserver — no fat interfaces.
    D - Dependency Inversion: FoodDeliveryFacade depends on service abstractions, OrderService depends on PaymentMethod ABC not concrete classes.
'''

from enum import Enum
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List, Dict, Optional


# ======================== Enums ========================

class OrderStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    PREPARING = "PREPARING"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


class PaymentStatus(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class CuisineType(Enum):
    ITALIAN = "ITALIAN"
    CHINESE = "CHINESE"
    INDIAN = "INDIAN"
    MEXICAN = "MEXICAN"


class MealType(Enum):
    VEG = "VEG"
    NON_VEG = "NON_VEG"


# ======================== Models ========================

class Address:
    def __init__(self, address_id: str, city: str, zipcode: str, location: str):
        self.address_id = address_id
        self.city = city
        self.zipcode = zipcode
        self.location = location


class User:
    def __init__(self, user_id: str, name: str, phone: str, address: Address):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.address = address


class DeliveryBoy:
    def __init__(self, boy_id: str, name: str, phone: str):
        self.boy_id = boy_id
        self.name = name
        self.phone = phone
        self.available = True


class MenuItem:
    def __init__(self, item_id: str, name: str, cuisine: CuisineType, meal_type: MealType, price: float):
        self.item_id = item_id
        self.name = name
        self.cuisine = cuisine
        self.meal_type = meal_type
        self.price = price


class Restaurant:
    def __init__(self, restaurant_id: str, name: str, address: Address):
        self.restaurant_id = restaurant_id
        self.name = name
        self.address = address
        self.menu_items: List[MenuItem] = []

    def add_menu_item(self, item: MenuItem):
        self.menu_items.append(item)

    def update_menu_item(self, item_id: str, updated: MenuItem):
        for i, item in enumerate(self.menu_items):
            if item.item_id == item_id:
                self.menu_items[i] = updated
                return
        raise ValueError(f"Menu item {item_id} not found")

    def get_items_by_meal_type(self, meal_type: MealType) -> List[MenuItem]:
        return [item for item in self.menu_items if item.meal_type == meal_type]

    def get_items_by_cuisine(self, cuisine: CuisineType) -> List[MenuItem]:
        return [item for item in self.menu_items if item.cuisine == cuisine]


class Bill:
    def __init__(self, bill_id: str, total_cost: float, discount: float, tax: float):
        self.bill_id = bill_id
        self.total_cost = total_cost
        self.discount = discount
        self.tax = tax
        self.amount_to_pay = (total_cost - discount) + tax

    def __repr__(self):
        return (f"Bill(total={self.total_cost:.2f}, discount={self.discount:.2f}, "
                f"tax={self.tax:.2f}, pay={self.amount_to_pay:.2f})")


class Order:
    def __init__(self, order_id: str, user_id: str, restaurant_id: str, items: List[MenuItem], bill: Bill):
        self.order_id = order_id
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.items = items
        self.bill = bill
        self.status = OrderStatus.PENDING
        self.delivery_boy_id: Optional[str] = None
        self.timestamp = datetime.now()


class Cart:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def remove_item(self, item_id: str):
        for i, item in enumerate(self.items):
            if item.item_id == item_id:
                self.items.pop(i)
                return
        raise ValueError(f"Item {item_id} not in cart")

    def get_items(self) -> List[MenuItem]:
        return list(self.items)

    def get_total(self) -> float:
        return sum(item.price for item in self.items)

    def clear(self):
        self.items = []


class Coupon:
    def __init__(self, code: str, strategy: 'PricingStrategy', min_order: float = 0.0):
        self.code = code
        self.strategy = strategy
        self.min_order = min_order
        self.active = True


# ======================== Abstractions (OCP + DIP + ISP) ========================

class PricingStrategy(ABC):
    """Open/Closed — extend with new strategies without modifying existing ones."""
    @abstractmethod
    def calculate_price(self, amount: float) -> float:
        pass


class PaymentMethod(ABC):
    """Interface Segregation — payment is its own abstraction, not mixed into Order."""
    @abstractmethod
    def pay(self, amount: float) -> PaymentStatus:
        pass


class NotificationObserver(ABC):
    """Open/Closed — add new notification channels without changing OrderService."""
    @abstractmethod
    def notify(self, message: str):
        pass


# ======================== Strategy Implementations (LSP) ========================

class PercentageOffStrategy(PricingStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def calculate_price(self, amount: float) -> float:
        return amount * (1 - self.percentage / 100)


class FixedAmountOffStrategy(PricingStrategy):
    def __init__(self, discount: float):
        self.discount = discount

    def calculate_price(self, amount: float) -> float:
        return max(0, amount - self.discount)


class NoDiscountStrategy(PricingStrategy):
    def calculate_price(self, amount: float) -> float:
        return amount


# ======================== Payment Implementations (LSP) ========================

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float) -> PaymentStatus:
        print(f"Paid {amount:.2f} via Credit Card ending {self.card_number[-4:]}")
        return PaymentStatus.SUCCESS


class WalletPayment(PaymentMethod):
    def __init__(self, wallet_id: str, balance: float):
        self.wallet_id = wallet_id
        self.balance = balance

    def pay(self, amount: float) -> PaymentStatus:
        if self.balance >= amount:
            self.balance -= amount
            print(f"Paid {amount:.2f} via Wallet {self.wallet_id}. Remaining: {self.balance:.2f}")
            return PaymentStatus.SUCCESS
        print(f"Wallet {self.wallet_id} has insufficient balance")
        return PaymentStatus.FAILED


# ======================== Notification Implementations (LSP) ========================

class SMSNotification(NotificationObserver):
    def notify(self, message: str):
        print(f"[SMS] {message}")


class EmailNotification(NotificationObserver):
    def notify(self, message: str):
        print(f"[Email] {message}")


# ======================== Services (SRP — each class has ONE responsibility) ========================

class UserService:
    """SRP: Manages user CRUD only."""
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register(self, user: User):
        self.users[user.user_id] = user

    def get(self, user_id: str) -> User:
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        return self.users[user_id]

    def update(self, user_id: str, name: Optional[str] = None, phone: Optional[str] = None, address: Optional[Address] = None):
        user = self.get(user_id)
        if name:
            user.name = name
        if phone:
            user.phone = phone
        if address:
            user.address = address

    def delete(self, user_id: str):
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        del self.users[user_id]


class RestaurantService:
    """SRP: Manages restaurant registration and search."""
    def __init__(self):
        self.restaurants: Dict[str, Restaurant] = {}

    def register(self, restaurant: Restaurant):
        self.restaurants[restaurant.restaurant_id] = restaurant

    def get(self, restaurant_id: str) -> Restaurant:
        if restaurant_id not in self.restaurants:
            raise ValueError(f"Restaurant {restaurant_id} not found")
        return self.restaurants[restaurant_id]

    def search_by_name(self, name: str) -> List[Restaurant]:
        query = name.lower()
        return [r for r in self.restaurants.values() if query in r.name.lower()]

    def search_by_city(self, city: str) -> List[Restaurant]:
        query = city.lower()
        return [r for r in self.restaurants.values() if query in r.address.city.lower()]

    def get_menu(self, restaurant_id: str) -> List[MenuItem]:
        return self.get(restaurant_id).menu_items

    def get_menu_by_meal_type(self, restaurant_id: str, meal_type: MealType) -> List[MenuItem]:
        return self.get(restaurant_id).get_items_by_meal_type(meal_type)

    def get_menu_by_cuisine(self, restaurant_id: str, cuisine: CuisineType) -> List[MenuItem]:
        return self.get(restaurant_id).get_items_by_cuisine(cuisine)


class CartService:
    """SRP: Manages cart operations only."""
    def __init__(self):
        self.carts: Dict[str, Cart] = {}

    def get_or_create(self, user_id: str) -> Cart:
        if user_id not in self.carts:
            self.carts[user_id] = Cart(user_id)
        return self.carts[user_id]

    def add_item(self, user_id: str, item: MenuItem):
        self.get_or_create(user_id).add_item(item)

    def remove_item(self, user_id: str, item_id: str):
        self.get_or_create(user_id).remove_item(item_id)

    def get_items(self, user_id: str) -> List[MenuItem]:
        return self.get_or_create(user_id).get_items()

    def get_total(self, user_id: str) -> float:
        return self.get_or_create(user_id).get_total()

    def clear(self, user_id: str):
        self.get_or_create(user_id).clear()


class CouponService:
    """SRP: Manages coupon creation and validation."""
    def __init__(self):
        self.coupons: Dict[str, Coupon] = {}

    def add_coupon(self, coupon: Coupon):
        self.coupons[coupon.code] = coupon

    def apply_coupon(self, code: str, order_total: float) -> PricingStrategy:
        if code not in self.coupons:
            raise ValueError(f"Coupon '{code}' not found")
        coupon = self.coupons[code]
        if not coupon.active:
            raise ValueError(f"Coupon '{code}' is expired")
        if order_total < coupon.min_order:
            raise ValueError(f"Minimum order {coupon.min_order} required for coupon '{code}'")
        return coupon.strategy

    def deactivate(self, code: str):
        if code in self.coupons:
            self.coupons[code].active = False


class OrderService:
    """SRP: Manages order placement, cancellation, status tracking.
       DIP: Depends on PaymentMethod abstraction, not concrete payment classes."""
    def __init__(self, cart_service: CartService, observers: Optional[List[NotificationObserver]] = None):
        self.orders: Dict[str, Order] = {}
        self.cart_service = cart_service
        self.observers = observers or []

    def _notify_all(self, message: str):
        for obs in self.observers:
            obs.notify(message)

    def place_order(self, user_id: str, restaurant_id: str, payment: PaymentMethod, strategy: PricingStrategy = None) -> Order:
        cart = self.cart_service.get_or_create(user_id)
        if not cart.items:
            raise ValueError("Cart is empty!")

        strategy = strategy or NoDiscountStrategy()

        raw_total = cart.get_total()
        discounted = strategy.calculate_price(raw_total)
        tax = discounted * 0.05
        bill = Bill(f"BILL-{datetime.now().timestamp()}", raw_total, raw_total - discounted, tax)

        # Process payment
        status = payment.pay(bill.amount_to_pay)
        if status != PaymentStatus.SUCCESS:
            raise ValueError("Payment failed — order not placed")

        order_id = f"ORD-{datetime.now().timestamp()}"
        order = Order(order_id, user_id, restaurant_id, cart.get_items(), bill)
        order.status = OrderStatus.CONFIRMED
        self.orders[order_id] = order
        self.cart_service.clear(user_id)

        self._notify_all(f"Order {order_id} confirmed for user {user_id}. Total: {bill.amount_to_pay:.2f}")
        return order

    def cancel_order(self, order_id: str) -> Order:
        order = self._get_order(order_id)
        if order.status in (OrderStatus.OUT_FOR_DELIVERY, OrderStatus.DELIVERED):
            raise ValueError(f"Cannot cancel order in {order.status.value} state")
        order.status = OrderStatus.CANCELLED
        self._notify_all(f"Order {order_id} has been cancelled")
        return order

    def update_status(self, order_id: str, status: OrderStatus) -> Order:
        order = self._get_order(order_id)
        order.status = status
        self._notify_all(f"Order {order_id} status updated to {status.value}")
        return order

    def get_order(self, order_id: str) -> Order:
        return self._get_order(order_id)

    def get_user_orders(self, user_id: str) -> List[Order]:
        return [o for o in self.orders.values() if o.user_id == user_id]

    def _get_order(self, order_id: str) -> Order:
        if order_id not in self.orders:
            raise ValueError(f"Order {order_id} not found")
        return self.orders[order_id]


class DeliveryService:
    """SRP: Manages delivery boy registration, assignment, and tracking."""
    def __init__(self, order_service: OrderService, observers: Optional[List[NotificationObserver]] = None):
        self.delivery_boys: Dict[str, DeliveryBoy] = {}
        self.order_service = order_service
        self.observers = observers or []

    def _notify_all(self, message: str):
        for obs in self.observers:
            obs.notify(message)

    def register(self, boy: DeliveryBoy):
        self.delivery_boys[boy.boy_id] = boy

    def assign_delivery(self, order_id: str, boy_id: str):
        if boy_id not in self.delivery_boys:
            raise ValueError(f"Delivery boy {boy_id} not found")
        boy = self.delivery_boys[boy_id]
        if not boy.available:
            raise ValueError(f"Delivery boy {boy_id} is not available")

        order = self.order_service.get_order(order_id)
        order.delivery_boy_id = boy_id
        boy.available = False
        self.order_service.update_status(order_id, OrderStatus.OUT_FOR_DELIVERY)
        self._notify_all(f"Delivery boy {boy.name} assigned to order {order_id}")

    def complete_delivery(self, order_id: str):
        order = self.order_service.get_order(order_id)
        if not order.delivery_boy_id:
            raise ValueError("No delivery boy assigned to this order")
        boy = self.delivery_boys[order.delivery_boy_id]
        boy.available = True
        self.order_service.update_status(order_id, OrderStatus.DELIVERED)

    def get_deliveries_by_boy(self, boy_id: str) -> List[Order]:
        return [o for o in self.order_service.orders.values() if o.delivery_boy_id == boy_id]


# ======================== Facade (DIP — depends on service abstractions) ========================

class FoodDeliveryFacade:
    """Facade that wires all services together for a clean public API."""
    def __init__(self):
        self.observers: List[NotificationObserver] = [SMSNotification()]
        self.user_service = UserService()
        self.restaurant_service = RestaurantService()
        self.cart_service = CartService()
        self.coupon_service = CouponService()
        self.order_service = OrderService(self.cart_service, self.observers)
        self.delivery_service = DeliveryService(self.order_service, self.observers)


# ======================== Demo ========================

if __name__ == "__main__":

    app = FoodDeliveryFacade()

    # --- Users ---
    delhi_addr = Address("A1", "New Delhi", "110001", "28.61, 77.20")
    user = User("U1", "John Doe", "9876543210", delhi_addr)
    app.user_service.register(user)

    # --- Restaurants ---
    rest1 = Restaurant("R1", "The Pizza Place", delhi_addr)
    pizza = MenuItem("I1", "Margherita Pizza", CuisineType.ITALIAN, MealType.VEG, 500.0)
    pasta = MenuItem("I2", "Penne Arrabiata", CuisineType.ITALIAN, MealType.VEG, 350.0)
    rest1.add_menu_item(pizza)
    rest1.add_menu_item(pasta)
    app.restaurant_service.register(rest1)

    mumbai_addr = Address("A2", "Mumbai", "400001", "19.07, 72.87")
    rest2 = Restaurant("R2", "Dragon Wok", mumbai_addr)
    noodles = MenuItem("I3", "Hakka Noodles", CuisineType.CHINESE, MealType.VEG, 250.0)
    rest2.add_menu_item(noodles)
    app.restaurant_service.register(rest2)

    # --- Search restaurants ---
    print("=== Search by name 'pizza' ===")
    for r in app.restaurant_service.search_by_name("pizza"):
        print(f"  {r.name}")

    print("=== Search by city 'delhi' ===")
    for r in app.restaurant_service.search_by_city("delhi"):
        print(f"  {r.name}")

    # --- Browse menu ---
    print("\n=== VEG items at The Pizza Place ===")
    for item in app.restaurant_service.get_menu_by_meal_type("R1", MealType.VEG):
        print(f"  {item.name} — ₹{item.price}")

    # --- Cart operations ---
    app.cart_service.add_item("U1", pizza)
    app.cart_service.add_item("U1", pasta)
    print(f"\nCart items: {[i.name for i in app.cart_service.get_items('U1')]}")
    print(f"Cart total: ₹{app.cart_service.get_total('U1')}")

    app.cart_service.remove_item("U1", "I2")
    print(f"After removing pasta: {[i.name for i in app.cart_service.get_items('U1')]}")

    # Re-add for the order
    app.cart_service.add_item("U1", pasta)

    # --- Coupons ---
    promo = Coupon("SAVE10", PercentageOffStrategy(10), min_order=200)
    flat100 = Coupon("FLAT100", FixedAmountOffStrategy(100), min_order=500)
    app.coupon_service.add_coupon(promo)
    app.coupon_service.add_coupon(flat100)

    strategy = app.coupon_service.apply_coupon("SAVE10", app.cart_service.get_total("U1"))

    # --- Place order with payment ---
    print("\n=== Placing Order ===")
    card = CreditCardPayment("4111111111111234")
    order = app.order_service.place_order("U1", "R1", card, strategy)
    print(f"Order ID: {order.order_id}, Status: {order.status.value}")
    print(f"Bill: {order.bill}")

    # --- Delivery boy ---
    boy = DeliveryBoy("D1", "Ravi", "9999999999")
    app.delivery_service.register(boy)
    app.delivery_service.assign_delivery(order.order_id, "D1")
    print(f"\nOrder status after dispatch: {order.status.value}")

    app.delivery_service.complete_delivery(order.order_id)
    print(f"Order status after delivery: {order.status.value}")

    print(f"Deliveries by D1: {[o.order_id for o in app.delivery_service.get_deliveries_by_boy('D1')]}")

    # --- Cancel order demo ---
    app.cart_service.add_item("U1", noodles)
    wallet = WalletPayment("W1", 5000.0)
    order2 = app.order_service.place_order("U1", "R2", wallet)

    print(f"\n=== Cancelling Order {order2.order_id} ===")
    app.order_service.cancel_order(order2.order_id)
    print(f"Order status: {order2.status.value}")

    # --- User orders ---
    print(f"\nAll orders by U1: {[(o.order_id, o.status.value) for o in app.order_service.get_user_orders('U1')]}")