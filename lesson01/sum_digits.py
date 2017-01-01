def sum_digits(number):
    """Calculate sum of the digits of the integer number"""
    result = 0
    if (number < 0):
        number = -number
    while (number > 0):
        result += number % 10
        number //= 10

    return result

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    result = sum_digits(number)
    print("Sum of the {} digits: {}".format(number, result))
