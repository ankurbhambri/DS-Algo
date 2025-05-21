from collections import deque


def min_operations_to_target(digits, target):
    # Convert digit strings to integers
    digits = [int(d) for d in digits]

    # Initialize BFS queue and visited set
    queue = deque([(d, 0) for d in digits])
    visited = set(digits)

    # BFS loop
    while queue:
        current_value, operations = queue.popleft()

        # Check if we've reached the target
        if current_value == target:
            return operations

        # Generate new values by applying +, -, and * operations
        for digit in digits:
            new_values = [
                current_value + digit,
                current_value - digit,
                current_value * digit,
            ]

            for new_value in new_values:
                # Only process new values within the valid range and not yet visited
                if 0 <= new_value <= 99999 and new_value not in visited:
                    queue.append((new_value, operations + 1))
                    visited.add(new_value)

    # If we exhaust the queue without finding the target, return -1
    return -1


# Examples
print(min_operations_to_target(["1"], 1))  # Output: 0
print(min_operations_to_target(["1"], 11))  # Output: 10
print(min_operations_to_target(["1"], 21))  # Output: 20
