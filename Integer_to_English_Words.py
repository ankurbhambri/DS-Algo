def numberToWords(num):

    if num == 0:
        return "Zero"

    # Define words for numbers up to 19, tens, and larger units
    below_20 = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    tens = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    thousands = ["", "Thousand", "Million", "Billion"]

    # Helper function to convert numbers less than 1000 to words
    def helper(num):
        if num == 0:
            return ""
        elif num < 20:
            return below_20[num] + " "
        elif num < 100:
            return tens[num // 10] + " " + helper(num % 10)
        else:
            return below_20[num // 100] + " Hundred " + helper(num % 100)

    result = ""
    for i, unit in enumerate(thousands):
        if num == 0:
            break
        if num % 1000 != 0:
            result = helper(num % 1000) + unit + " " + result
        num //= 1000

    return result.strip()


print(numberToWords(123))
print(numberToWords(12345))
print(numberToWords(1234567))
