from abc import ABC, abstractmethod

# In case customer is manually converting weight from pounds to kilograms, 
# we can use the adapter pattern to automate this process. 
# The adapter pattern allows us to convert the interface of a class into another interface that clients expect.
# In this example, we will create an adapter that converts weight from pounds to kilograms.


class WtMachine():  # adaptee
    def __init__(self):
        self.weight = 0

    def get_weight_pounds(self):
        return self.weight


class IAdapter(ABC): # target interface
    @abstractmethod
    def get_weight_kilograms(self):
        pass


class Adapter(IAdapter): # adapter
    def __init__(self, wt_machine: WtMachine):
        self.wt_machine = wt_machine

    def get_weight_kilograms(self):
        return self.wt_machine.get_weight_pounds() * 0.453592


wt_machine = WtMachine()
wt_machine.weight = 150  # Set weight in pounds
adapter = Adapter(wt_machine)
print(f"Weight in pounds: {wt_machine.get_weight_pounds()} lbs")
print(f"Weight in kilograms: {adapter.get_weight_kilograms():.2f} kg")