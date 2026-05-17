from __future__ import annotations
from abc import ABC, abstractmethod


# ------------------------------
# 1) Singleton Pattern
# ------------------------------
class AppConfig:

	_instance: AppConfig | None = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance.theme = "light"
		return cls._instance


'''
Difference between factory and strategy:
- Factory focuses on creating objects based on input parameters, while Strategy focuses on changing the behavior of an object at runtime.
- Factory abstracts the instantiation process, while Strategy abstracts the algorithm/behavior itself.
- Factory is about "what to create", while Strategy is about "how to do it".
'''

# ------------------------------
# 2) Factory Pattern: It is a creational design pattern that deals with HOW an object can be created at runtime.
# ------------------------------
class Notification(ABC):
	@abstractmethod
	def send(self, message: str) -> str:
		raise NotImplementedError


class EmailNotification(Notification):
	def send(self, message: str) -> str:
		return f"Email sent: {message}"


class SmsNotification(Notification):
	def send(self, message: str) -> str:
		return f"SMS sent: {message}"


class NotificationFactory:
	@staticmethod
	def create(channel: str) -> Notification:
		channel = channel.lower()
		if channel == "email":
			return EmailNotification()
		if channel == "sms":
			return SmsNotification()
		raise ValueError(f"Unsupported channel: {channel}")


# ------------------------------
# 3) Strategy Pattern: It is used to change the algo/behavior at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable.
# ------------------------------
class PaymentStrategy(ABC):
	@abstractmethod
	def pay(self, amount: float) -> str:
		raise NotImplementedError


class CardPayment(PaymentStrategy):
	def pay(self, amount: float) -> str:
		return f"Paid ${amount:.2f} using Card"


class UpiPayment(PaymentStrategy):
	def pay(self, amount: float) -> str:
		return f"Paid ${amount:.2f} using UPI"


class Checkout:
	def __init__(self, strategy: PaymentStrategy):
		self.strategy = strategy

	def set_strategy(self, strategy: PaymentStrategy) -> None:
		self.strategy = strategy

	def process(self, amount: float) -> str:
		return self.strategy.pay(amount)


print("=== Singleton Demo ===")
config1 = AppConfig()
config2 = AppConfig()
print("Same instance?", config1 is config2)
config1.theme = "dark"
print("config2.theme after config1 change:", config2.theme)

print("\n=== Factory Demo ===")
notifier = NotificationFactory.create("email")
print(notifier.send("Welcome to the platform"))
notifier = NotificationFactory.create("sms")
print(notifier.send("Your OTP is 1234"))

print("\n=== Strategy Demo ===")
checkout = Checkout(CardPayment())
print(checkout.process(199.0))
checkout.set_strategy(UpiPayment())
print(checkout.process(199.0))