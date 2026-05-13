from abc import ABC, abstractmethod

'''
The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. 
Abstractions should not depend on details. Details should depend on abstractions.

InCorrect approach: Below approach violates the dependency inversion principle because PowerSwitch (high-level module) directly depends on LightBulb (low-level module).

class LightBulb:
    def turn_on(self):
        print("LightBulb is turned on")

    def turn_off(self):
        print("LightBulb is turned off")

class PowerSwitch:
    def __init__(self, c: LightBulb):
        self.c = c
        self.on = False

    def press(self):
        if self.on:
            self.c.turn_off()
            self.on = False
        else:
            self.c.turn_on()
            self.on = True
'''

# Correct approach: Below approach adheres to the dependency inversion principle because PowerSwitch (high-level module) depends on the abstraction (Switch),
# rather than the concrete implementation (LightBulb).

class Switch(ABC):

    @abstractmethod
    def turn_on(self):
        print("Switch is turned on")

    @abstractmethod
    def turn_off(self):
        print("Switch is turned off")


class LightBulb(Switch):

    def turn_on(self):
        print("LightBulb is turned on")

    def turn_off(self):
        print("LightBulb is turned off")


class PowerSwitch:

    def __init__(self, c: Switch):
        self.c = c
        self.on = False

    def press(self):
        if self.on:
            self.c.turn_off()
            self.on = False
        else:
            self.c.turn_on()
            self.on = True

# usage
light_bulb = LightBulb()
switch = PowerSwitch(light_bulb)
switch.press()  # Output: Switch is turned on, LightBulb is turned on
switch.press()  # Output: Switch is turned off, LightBulb is turned off