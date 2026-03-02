"""
Write a program that allows the user to calculate the price of a pizza. A pizza has:

- a base
- a size
- toppings
- coupons
- billing

Assume the system stores everything in-memory, no storage required

"""

from enum import Enum
from abc import ABC, abstractmethod

# =========================
# ENUMS
# =========================

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Type(Enum):
    VEG = 1
    NONVEG = 2

# =========================
# PIZZA ABSTRACTION
# =========================

class Pizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_base(self):
        pass

# =========================
# BASE PIZZA
# =========================

class BasePizza(Pizza):

    SIZE_PRICE = {
        Size.SMALL: 100,
        Size.MEDIUM: 200,
        Size.LARGE: 300
    }

    def __init__(self, size: Size, pizza_type: Type):
        self.size = size
        self.type = pizza_type

    def get_cost(self):
        return self.SIZE_PRICE[self.size]

    def get_base(self):
        return self

    def is_non_veg(self):
        return self.type == Type.NONVEG

# =========================
# TOPPING DECORATOR
# =========================

class Topping(Pizza):

    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()

    def get_base(self):
        return self.pizza.get_base()

class Cheese(Topping):
    def get_cost(self):
        return super().get_cost() + 30

class Mushroom(Topping):
    def get_cost(self):
        return super().get_cost() + 20

class Pepperoni(Topping):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

        # validation
        if not self.get_base().is_non_veg():
            raise ValueError("Pepperoni allowed only on Non-Veg pizza")

    def get_cost(self):
        return super().get_cost() + 50

# =========================
# COUPONS
# =========================

class Coupon(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float:
        pass

class FlatCoupon(Coupon):
    def __init__(self, discount: float):
        self.discount = discount

    def apply(self, amount):
        return min(self.discount, amount)

class PercentageCoupon(Coupon):
    def __init__(self, percent: float, min_amount: float = 0):
        self.percent = percent
        self.min_amount = min_amount

    def apply(self, amount):
        if amount >= self.min_amount:
            return amount * self.percent / 100
        return 0

# =========================
# BILLING SERVICE
# =========================

class BillingService:

    TAX_PERCENT = 10
    DELIVERY_CHARGE = 100
    FREE_DELIVERY_ABOVE = 1000

    def generate_bill(self, items, coupon: Coupon = None):

        subtotal = sum(item.get_cost() for item in items)

        discount = coupon.apply(subtotal) if coupon else 0
        amount_after_discount = subtotal - discount

        tax = amount_after_discount * self.TAX_PERCENT / 100

        if amount_after_discount >= self.FREE_DELIVERY_ABOVE:
            delivery = 0
        else:
            delivery = self.DELIVERY_CHARGE

        final_amount = amount_after_discount + tax + delivery

        return {
            "Subtotal": subtotal,
            "Discount": discount,
            "Tax": tax,
            "Delivery": delivery,
            "Final Amount": final_amount
        }

# =========================
# CART
# =========================

class Cart:

    def __init__(self):
        self.items = []

    def add(self, pizza: Pizza):
        self.items.append(pizza)

    def checkout(self, billing_service: BillingService, coupon: Coupon = None):
        return billing_service.generate_bill(self.items, coupon)

# =========================
# DEMO
# =========================

def main():

    cart = Cart()

    pizza1 = BasePizza(Size.MEDIUM, Type.VEG)
    pizza1 = Cheese(pizza1)
    pizza1 = Mushroom(pizza1)

    pizza2 = BasePizza(Size.LARGE, Type.NONVEG)
    pizza2 = Pepperoni(pizza2)

    cart.add(pizza1)
    cart.add(pizza2)

    coupon = PercentageCoupon(10, min_amount=500)

    billing_service = BillingService()

    bill = cart.checkout(billing_service, coupon)

    for k, v in bill.items():
        print(f"{k}: {v:.2f}")

if __name__ == "__main__":
    main()