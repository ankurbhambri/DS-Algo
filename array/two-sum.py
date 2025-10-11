# Design and implement a data structure that supports adding a number and checking if a particular sum of any two numbers exists. 
# Basically, think of a class with an add method to add a number and a find method to find if there's a pair of numbers that sum up to a given value

class TwoSum:
    def __init__(self):
        # Dictionary to store numbers and their frequencies
        self.num_counts = {}

    def add(self, number: int) -> None:
        """Add a number to the data structure."""
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, target: int) -> bool:

        """Check if there exists a pair of numbers that sum up to 'target'."""

        for num in self.num_counts:

            complement = target - num

            if complement == num:

                if self.num_counts[num] > 1:
                    return True

            elif complement in self.num_counts:

                return True

        return False


ts = TwoSum()
ts.add(1)
ts.add(3)
ts.add(5)

print(ts.find(4))  # True (1 + 3)
print(ts.find(7))  # False (no two numbers sum to 7)
print(ts.find(6))  # True (1 + 5)