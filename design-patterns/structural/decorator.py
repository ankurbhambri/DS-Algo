from abc import ABC, abstractmethod

# Step 1: Component Interface
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# Step 2: Concrete Component
class Margherita(Pizza):
    def get_description(self) -> str:
        return "Margherita"

    def get_cost(self) -> float:
        return 5.00

class Farmhouse(Pizza):
    def get_description(self) -> str:
        return "Farmhouse"

    def get_cost(self) -> float:
        return 7.00


# Step 3: Decorator Base Class
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_description(self) -> str:
        return self._pizza.get_description()

    def get_cost(self) -> float:
        return self._pizza.get_cost()

# Step 4: Concrete Decorators
class Cheese(PizzaDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.25

class Olives(PizzaDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Olives"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.75

class Mushrooms(PizzaDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Mushrooms"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.50


if __name__ == "__main__":
    # Start with a base pizza
    pizza = Margherita()

    # Add toppings dynamically using decorators
    pizza = Cheese(pizza)
    pizza = Olives(pizza)
    pizza = Mushrooms(pizza)

    # Final pizza description and cost
    print(f"Pizza Description: {pizza.get_description()}")
    print(f"Total Cost: ${pizza.get_cost():.2f}")
