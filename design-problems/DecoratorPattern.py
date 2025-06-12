from abc import ABC, abstractmethod

# -----------------------------
#     Common Interface
# -----------------------------
class OrderItem(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

# -----------------------------
#     Pizza Hierarchy
# -----------------------------
class Pizza(OrderItem):
    pass

class Margherita(Pizza):
    def get_cost(self) -> float:
        return 5.00

    def get_description(self) -> str:
        return "Margherita"

class Farmhouse(Pizza):
    def get_cost(self) -> float:
        return 6.00

    def get_description(self) -> str:
        return "Farmhouse"

# Pizza Decorators
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

class Cheese(PizzaDecorator):
    def get_cost(self):
        return self._pizza.get_cost() + 1.00

    def get_description(self):
        return self._pizza.get_description() + ", Cheese"

class Olives(PizzaDecorator):
    def get_cost(self):
        return self._pizza.get_cost() + 0.75

    def get_description(self):
        return self._pizza.get_description() + ", Olives"

# -----------------------------
#     Beverage Hierarchy
# -----------------------------
class Beverage(OrderItem):
    pass

class Coke(Beverage):
    def get_cost(self) -> float:
        return 2.00

    def get_description(self) -> str:
        return "Coke"

class Coffee(Beverage):
    def get_cost(self) -> float:
        return 3.00

    def get_description(self) -> str:
        return "Coffee"

# Beverage Decorators
class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

class Ice(BeverageDecorator):
    def get_cost(self):
        return self._beverage.get_cost() + 0.25

    def get_description(self):
        return self._beverage.get_description() + ", Ice"

class ExtraSugar(BeverageDecorator):
    def get_cost(self):
        return self._beverage.get_cost() + 0.15

    def get_description(self):
        return self._beverage.get_description() + ", Extra Sugar"

# -----------------------------
#     Pizza Factory
# -----------------------------
class PizzaFactory:
    @staticmethod
    def create_margherita_with_cheese_and_olives() -> Pizza:
        pizza = Margherita()
        pizza = Cheese(pizza)
        pizza = Olives(pizza)
        return pizza

    @staticmethod
    def create_farmhouse_cheese() -> Pizza:
        pizza = Farmhouse()
        pizza = Cheese(pizza)
        return pizza

# -----------------------------
#     Beverage Factory
# -----------------------------
class BeverageFactory:
    @staticmethod
    def create_coke_with_ice_and_sugar() -> Beverage:
        drink = Coke()
        drink = Ice(drink)
        drink = ExtraSugar(drink)
        return drink

    @staticmethod
    def create_black_coffee() -> Beverage:
        return Coffee()


# Test cases
order: list[OrderItem] = []

# Factory usage
pizza1 = PizzaFactory.create_margherita_with_cheese_and_olives()
pizza2 = PizzaFactory.create_farmhouse_cheese()
beverage1 = BeverageFactory.create_coke_with_ice_and_sugar()
beverage2 = BeverageFactory.create_black_coffee()

order.extend([pizza1, pizza2, beverage1, beverage2])

print("Order Summary:")
total = 0.0
for item in order:
    print(f"- {item.get_description()} (${item.get_cost():.2f})")
    total += item.get_cost()

print(f"\nTotal: ${total:.2f}")
