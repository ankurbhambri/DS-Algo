'''
Design Stock Broker Platform Like Zerodha, Groww

You are asked to design a simplified version of a stock brokerage platform like Zerodha or Groww. 
This platform will allow users to buy and sell stocks, maintain their portfolio, and view order history. You need to focus on core functionalities and write clean, extensible code.

Requirements:

- Create a user and associate a trading account with an initial cash balance.
- Fetch account details (name, cash balance, portfolio).

- Maintain a list of tradable stocks (symbol, name, current price).
- Prices can be mocked or randomly generated.


- A user can place BUY or SELL orders.
- Orders can be of type MARKET or LIMIT.
- Before placing an order:
- Check if the user has enough balance (for BUY).
- Check if the user has enough quantity (for SELL).


- For MARKET orders: execute immediately at current price.
- For LIMIT orders: execute immediately if market conditions allow; otherwise keep it pending.
- Update user’s cash balance and stock holdings after an order is executed.


- Show current holdings with quantities and average prices.
- Show a list of all orders placed, along with their status (FILLED, PENDING, REJECTED).

Basic APIs / Methods

- createUser(name, initialBalance)
- listStocks()
- placeOrder(userId, symbol, type, side, quantity, price)
- getPortfolio(userId)
- getOrderHistory(userId)

Constraints:

- Single currency system (e.g., INR or USD).
- No partial fills — either the entire order executes or it stays pending.
- All data can be stored in memory for this problem.
- No need for multi-threading unless you want to show extra skills.


SOLID Principles applied:
    S - Single Responsibility: Separate services — UserService, StockService, OrderService, PortfolioService.
    O - Open/Closed: OrderExecutionStrategy ABC lets you add new order types without modifying existing logic.
    L - Liskov Substitution: MarketOrderStrategy and LimitOrderStrategy are interchangeable via base class.
    I - Interface Segregation: Small focused ABCs (OrderExecutionStrategy) — no fat interfaces.
    D - Dependency Inversion: BrokerPlatform and OrderService depend on abstractions, not concrete classes.
'''

from enum import Enum
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import random


# ======================== Enums ========================

class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"


class OrderStatus(Enum):
    FILLED = "FILLED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"


# ======================== Models ========================

class Stock:
    def __init__(self, symbol: str, name: str, price: float):
        self.symbol = symbol
        self.name = name
        self.price = price


class Holding:
    """Tracks quantity and average buy price of a stock in a user's portfolio."""
    def __init__(self, symbol: str, quantity: int, avg_price: float):
        self.symbol = symbol
        self.quantity = quantity
        self.avg_price = avg_price

    def add(self, quantity: int, price: float):
        total_cost = self.avg_price * self.quantity + price * quantity
        self.quantity += quantity
        self.avg_price = total_cost / self.quantity

    def remove(self, quantity: int):
        if quantity > self.quantity:
            raise ValueError(f"Not enough holdings to sell. Have {self.quantity}, want to sell {quantity}")
        self.quantity -= quantity


class TradingAccount:
    def __init__(self, user_id: str, balance: float):
        self.user_id = user_id
        self.balance = balance
        self.holdings: Dict[str, Holding] = {}

    def get_holding(self, symbol: str) -> Optional[Holding]:
        return self.holdings.get(symbol)

    def get_quantity(self, symbol: str) -> int:
        h = self.holdings.get(symbol)
        return h.quantity if h else 0


class User:
    def __init__(self, user_id: str, name: str, account: TradingAccount):
        self.user_id = user_id
        self.name = name
        self.account = account


class Order:
    def __init__(self, order_id: str, user_id: str, symbol: str, order_type: OrderType,
                 side: OrderSide, quantity: int, limit_price: Optional[float] = None):
        self.order_id = order_id
        self.user_id = user_id
        self.symbol = symbol
        self.order_type = order_type
        self.side = side
        self.quantity = quantity
        self.limit_price = limit_price
        self.executed_price: Optional[float] = None
        self.status = OrderStatus.PENDING
        self.timestamp = datetime.now()


# ======================== Strategy — Order Execution (OCP + LSP) ========================

class OrderExecutionStrategy(ABC):
    """Open/Closed: new order types can be added by subclassing, no modification needed."""
    @abstractmethod
    def can_execute(self, order: Order, market_price: float) -> bool:
        pass

    @abstractmethod
    def get_execution_price(self, order: Order, market_price: float) -> float:
        pass


class MarketOrderStrategy(OrderExecutionStrategy):
    def can_execute(self, order: Order, market_price: float) -> bool:
        return True

    def get_execution_price(self, order: Order, market_price: float) -> float:
        return market_price


class LimitOrderStrategy(OrderExecutionStrategy):
    def can_execute(self, order: Order, market_price: float) -> bool:
        if order.side == OrderSide.BUY:
            return market_price <= order.limit_price
        else:
            return market_price >= order.limit_price

    def get_execution_price(self, order: Order, market_price: float) -> float:
        return order.limit_price


# ======================== Services (SRP) ========================

class UserService:
    """SRP: User creation and lookup only."""
    def __init__(self):
        self._users: Dict[str, User] = {}
        self._counter = 0

    def create_user(self, name: str, initial_balance: float) -> User:
        self._counter += 1
        user_id = f"U{self._counter}"
        account = TradingAccount(user_id, initial_balance)
        user = User(user_id, name, account)
        self._users[user_id] = user
        return user

    def get_user(self, user_id: str) -> User:
        if user_id not in self._users:
            raise ValueError(f"User {user_id} not found")
        return self._users[user_id]

    def get_account_details(self, user_id: str) -> dict:
        user = self.get_user(user_id)
        return {
            "name": user.name,
            "balance": user.account.balance,
            "holdings": {
                sym: {"quantity": h.quantity, "avg_price": h.avg_price}
                for sym, h in user.account.holdings.items() if h.quantity > 0
            },
        }


class StockService:
    """SRP: Stock listing and price management only."""
    def __init__(self):
        self._stocks: Dict[str, Stock] = {}

    def add_stock(self, symbol: str, name: str, price: float):
        self._stocks[symbol] = Stock(symbol, name, price)

    def get_stock(self, symbol: str) -> Stock:
        if symbol not in self._stocks:
            raise ValueError(f"Stock {symbol} not found")
        return self._stocks[symbol]

    def list_stocks(self) -> List[Stock]:
        return list(self._stocks.values())

    def get_price(self, symbol: str) -> float:
        return self.get_stock(symbol).price

    def simulate_price_change(self):
        """Mock price fluctuation."""
        for stock in self._stocks.values():
            change = random.uniform(-0.05, 0.05)
            stock.price = round(stock.price * (1 + change), 2)


class PortfolioService:
    """SRP: Portfolio queries — delegates to UserService for data."""
    def __init__(self, user_service: UserService, stock_service: StockService):
        self._user_service = user_service
        self._stock_service = stock_service

    def get_portfolio(self, user_id: str) -> List[dict]:
        user = self._user_service.get_user(user_id)
        result = []
        for sym, holding in user.account.holdings.items():
            if holding.quantity == 0:
                continue
            current_price = self._stock_service.get_price(sym)
            result.append({
                "symbol": sym,
                "quantity": holding.quantity,
                "avg_price": round(holding.avg_price, 2),
                "current_price": current_price,
                "pnl": round((current_price - holding.avg_price) * holding.quantity, 2),
            })
        return result


class OrderService:
    """SRP: Order placement, execution and history.
       DIP: Depends on OrderExecutionStrategy abstraction, not concrete classes."""
    def __init__(self, user_service: UserService, stock_service: StockService):
        self._user_service = user_service
        self._stock_service = stock_service
        self._orders: List[Order] = []
        self._counter = 0

        # Strategy mapping — new order types only need a new entry here (OCP)
        self._strategies: Dict[OrderType, OrderExecutionStrategy] = {
            OrderType.MARKET: MarketOrderStrategy(),
            OrderType.LIMIT: LimitOrderStrategy(),
        }

    def place_order(self, user_id: str, symbol: str, order_type: OrderType,
                    side: OrderSide, quantity: int, limit_price: Optional[float] = None) -> Order:

        user = self._user_service.get_user(user_id)
        stock = self._stock_service.get_stock(symbol)
        market_price = stock.price

        self._counter += 1
        order = Order(f"ORD{self._counter}", user_id, symbol, order_type, side, quantity, limit_price)

        # --- Validate ---
        if side == OrderSide.BUY:
            cost = market_price * quantity
            if user.account.balance < cost:
                order.status = OrderStatus.REJECTED
                self._orders.append(order)
                return order
        else:
            if user.account.get_quantity(symbol) < quantity:
                order.status = OrderStatus.REJECTED
                self._orders.append(order)
                return order

        # --- Try to execute via strategy ---
        strategy = self._strategies[order_type]
        if strategy.can_execute(order, market_price):
            self._execute(order, user, strategy.get_execution_price(order, market_price))
        # else stays PENDING

        self._orders.append(order)
        return order

    def try_fill_pending(self):
        """Attempt to fill all pending limit orders against current prices."""
        for order in self._orders:
            if order.status != OrderStatus.PENDING:
                continue
            user = self._user_service.get_user(order.user_id)
            market_price = self._stock_service.get_price(order.symbol)
            strategy = self._strategies[order.order_type]
            if strategy.can_execute(order, market_price):
                # Re-validate before filling
                if order.side == OrderSide.BUY and user.account.balance < market_price * order.quantity:
                    continue
                if order.side == OrderSide.SELL and user.account.get_quantity(order.symbol) < order.quantity:
                    continue
                self._execute(order, user, strategy.get_execution_price(order, market_price))

    def cancel_order(self, order_id: str) -> Order:
        order = self._find_order(order_id)
        if order.status != OrderStatus.PENDING:
            raise ValueError(f"Only PENDING orders can be cancelled, current status: {order.status.value}")
        order.status = OrderStatus.CANCELLED
        return order

    def get_order_history(self, user_id: str) -> List[Order]:
        return [o for o in self._orders if o.user_id == user_id]

    # --- Private helpers ---

    def _execute(self, order: Order, user: User, price: float):
        total = price * order.quantity
        account = user.account

        if order.side == OrderSide.BUY:
            account.balance -= total
            if order.symbol in account.holdings:
                account.holdings[order.symbol].add(order.quantity, price)
            else:
                account.holdings[order.symbol] = Holding(order.symbol, order.quantity, price)
        else:
            account.balance += total
            account.holdings[order.symbol].remove(order.quantity)

        order.executed_price = price
        order.status = OrderStatus.FILLED

    def _find_order(self, order_id: str) -> Order:
        for o in self._orders:
            if o.order_id == order_id:
                return o
        raise ValueError(f"Order {order_id} not found")


# ======================== Facade (DIP — depends on service abstractions) ========================

class BrokerPlatform:
    """Facade that wires all services together for a clean public API."""
    def __init__(self):
        self.user_service = UserService()
        self.stock_service = StockService()
        self.portfolio_service = PortfolioService(self.user_service, self.stock_service)
        self.order_service = OrderService(self.user_service, self.stock_service)

    def create_user(self, name: str, initial_balance: float) -> User:
        return self.user_service.create_user(name, initial_balance)

    def list_stocks(self) -> List[Stock]:
        return self.stock_service.list_stocks()

    def place_order(self, user_id: str, symbol: str, order_type: OrderType,
                    side: OrderSide, quantity: int, limit_price: Optional[float] = None) -> Order:
        return self.order_service.place_order(user_id, symbol, order_type, side, quantity, limit_price)

    def get_portfolio(self, user_id: str) -> List[dict]:
        return self.portfolio_service.get_portfolio(user_id)

    def get_order_history(self, user_id: str) -> List[Order]:
        return self.order_service.get_order_history(user_id)


# ======================== Demo ========================

if __name__ == "__main__":

    platform = BrokerPlatform()

    # --- Seed stocks ---
    for sym, name, price in [("RELIANCE", "Reliance Industries", 2450.0),
                              ("TCS", "Tata Consultancy", 3500.0),
                              ("INFY", "Infosys", 1480.0),
                              ("HDFC", "HDFC Bank", 1650.0)]:
        platform.stock_service.add_stock(sym, name, price)

    print("=== Available Stocks ===")
    for s in platform.list_stocks():
        print(f"  {s.symbol:10s} {s.name:25s} ₹{s.price:.2f}")

    # --- Create users ---
    alice = platform.create_user("Alice", 100000.0)
    bob = platform.create_user("Bob", 50000.0)
    print(f"\nCreated: {alice.name} (bal ₹{alice.account.balance})")
    print(f"Created: {bob.name} (bal ₹{bob.account.balance})")

    # --- Market BUY ---
    print("\n=== Alice: Market BUY 10 RELIANCE ===")
    o1 = platform.place_order(alice.user_id, "RELIANCE", OrderType.MARKET, OrderSide.BUY, 10)
    print(f"  Status: {o1.status.value}, Exec Price: {o1.executed_price}, Balance: ₹{alice.account.balance}")

    # --- Market BUY — insufficient funds ---
    print("\n=== Alice: Market BUY 100 TCS (should be REJECTED) ===")
    o2 = platform.place_order(alice.user_id, "TCS", OrderType.MARKET, OrderSide.BUY, 100)
    print(f"  Status: {o2.status.value}")

    # --- Market SELL ---
    print("\n=== Alice: Market SELL 5 RELIANCE ===")
    o3 = platform.place_order(alice.user_id, "RELIANCE", OrderType.MARKET, OrderSide.SELL, 5)
    print(f"  Status: {o3.status.value}, Balance: ₹{alice.account.balance}")

    # --- Limit BUY (price too low, should stay PENDING) ---
    print("\n=== Bob: Limit BUY 5 INFY at ₹1400 (should be PENDING) ===")
    o4 = platform.place_order(bob.user_id, "INFY", OrderType.LIMIT, OrderSide.BUY, 5, limit_price=1400.0)
    print(f"  Status: {o4.status.value}")

    # --- Limit BUY (price >= market, should FILL) ---
    print("\n=== Bob: Limit BUY 3 INFY at ₹1500 (should FILL since market=1480) ===")
    o5 = platform.place_order(bob.user_id, "INFY", OrderType.LIMIT, OrderSide.BUY, 3, limit_price=1500.0)
    print(f"  Status: {o5.status.value}, Exec Price: {o5.executed_price}")

    # --- Simulate price drop & try filling pending ---
    print("\n=== Simulate price change and try filling pending orders ===")
    platform.stock_service._stocks["INFY"].price = 1380.0
    platform.order_service.try_fill_pending()
    print(f"  Bob's pending order now: {o4.status.value}, Exec Price: {o4.executed_price}")

    # --- Cancel an order ---
    print("\n=== Bob: Place a limit order then cancel it ===")
    o6 = platform.place_order(bob.user_id, "TCS", OrderType.LIMIT, OrderSide.BUY, 2, limit_price=3000.0)
    print(f"  Before cancel: {o6.status.value}")
    platform.order_service.cancel_order(o6.order_id)
    print(f"  After cancel: {o6.status.value}")

    # --- Sell more than owned (should REJECT) ---
    print("\n=== Bob: SELL 100 INFY (should be REJECTED) ===")
    o7 = platform.place_order(bob.user_id, "INFY", OrderType.MARKET, OrderSide.SELL, 100)
    print(f"  Status: {o7.status.value}")

    # --- Portfolio ---
    print("\n=== Alice's Portfolio ===")
    for h in platform.get_portfolio(alice.user_id):
        print(f"  {h['symbol']:10s} qty={h['quantity']}  avg=₹{h['avg_price']}  "
              f"current=₹{h['current_price']}  P&L=₹{h['pnl']}")

    print("\n=== Bob's Portfolio ===")
    for h in platform.get_portfolio(bob.user_id):
        print(f"  {h['symbol']:10s} qty={h['quantity']}  avg=₹{h['avg_price']}  "
              f"current=₹{h['current_price']}  P&L=₹{h['pnl']}")

    # --- Account details ---
    print(f"\n=== Alice's Account ===")
    print(f"  {platform.user_service.get_account_details(alice.user_id)}")

    # --- Order history ---
    print(f"\n=== Alice's Order History ===")
    for o in platform.get_order_history(alice.user_id):
        print(f"  {o.order_id} {o.side.value:4s} {o.symbol:10s} qty={o.quantity} "
              f"type={o.order_type.value:6s} status={o.status.value:8s} exec_price={o.executed_price}")

    print(f"\n=== Bob's Order History ===")
    for o in platform.get_order_history(bob.user_id):
        print(f"  {o.order_id} {o.side.value:4s} {o.symbol:10s} qty={o.quantity} "
              f"type={o.order_type.value:6s} status={o.status.value:8s} exec_price={o.executed_price}")