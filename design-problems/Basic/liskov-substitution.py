from abc import ABC, abstractmethod

# The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. 

'''
Voilation of Liskov Substitution Principle (LSP)

Suppose we have a Pizza class with a method calculate_price() that calculates the price based on the pizza's size

If we extend this class to create a SpecialPizza subclass with different pricing logic, 
it might violate LSP if it doesn't behave as expected when substituted for a regular pizza.


class FoodItem(ABC):
    @abstractmethod
    def calculate_price(self) -> int:
        pass

class Pizza(FoodItem):
    def __init__(self, size):
        self.size = size
    
    def calculate_price(self):
        # Calculate price based on size
        pass

class SpecialPizza(Pizza):
    def calculate_price(self):
        # Calculate special price logic
        pass

'''

# Now, both Pizza and SpecialPizza inherit directly from FoodItem, ensuring that they can be substituted for each other without issues. 

class FoodItem(ABC):
    @abstractmethod
    def calculate_price(self) -> int:
        pass

class Pizza(FoodItem):
    def calculate_price(self) -> int:
        return 1.0

class SpecialPizza(Pizza):
    def calculate_price(self) -> int:
        return 2.0 # 2x expensive than regular pizza

print(Pizza().calculate_price())  # Output: 1.0
print(SpecialPizza().calculate_price())  # Output: 2.0