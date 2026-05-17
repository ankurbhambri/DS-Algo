# The Liskov Substitution Principle states that objects of a superclass should be replaceable,
# with objects of its subclasses without affecting the correctness of the program.

'''
Voilation of Liskov Substitution Principle (LSP)

BAD DESIGN. Because code expecting Bird may fail.

class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Cannot fly")

'''

# Correct approach to LSP
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Sparrow(FlyingBird):
    pass

class Penguin(Bird):
    pass


# usage
def make_bird_fly(b: FlyingBird):
    b.fly()


make_bird_fly(Sparrow())  # Works fine
make_bird_fly(Penguin())  # Error, Penguin is not a FlyingBird