def print_integer(n):
    print(f"[{n}]", end="")


def print_integer_list(array):
    print("[", end="")
    print(", ".join(map(str, array)), end="")
    print("]", end="")


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = expected == output

    right_tick = "\u2713"
    wrong_tick = "\u2717"

    if result:
        print(f"{right_tick} Test #{test_case_number}")
    else:
        print(f"{wrong_tick} Test #{test_case_number}: Expected ", end="")
        print_integer_list(expected)
        print(" Your output: ", end="")
        print_integer_list(output)
        print()

    test_case_number += 1
