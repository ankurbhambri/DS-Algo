################ Interview Questions #############
# Question1
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = " + str(sum) + ", Product = " + str(product))


ar1 = [1, 2, 3, 4]
foo(ar1)

# Question2


def printPairs(array):
    for i in array:
        for j in array:
            print(str(i) + "," + str(j))


# Question3
def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(array[i] + "," + array[j])


# Question4
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))


arrayA = [1, 2, 3, 4, 5]
arrayB = [2, 6, 7, 8]


# Question5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))


# printUnorderedPairss(arrayA,arrayB)


# Question6
def reverse(array):
    for i in range(0, int(len(array) / 2)):

        array[len(array) - i - 1], array[i] = (
            array[i],
            array[len(array) - i - 1],
        )
    return array


print("reversed array ", reverse(arrayA))


# Question8
def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))


# Question9
def allFib(n):
    for i in range(n):
        print(str(i) + ":, " + str(fib(i)))


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


allFib(4)


# Question10
def powersOf2(n):
    # print("n:"+str(n))
    if n < 1:
        return 0
    elif n == 1:
        # print(1)
        return 1
    else:
        prev = powersOf2(int(n / 2))
        # print("prev:"+str(prev))
        # print(prev)
        curr = prev * 2
        # print(curr)
        return curr


print(powersOf2(50))
