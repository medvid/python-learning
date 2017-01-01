from sum_digits import sum_digits

def count_happy_tickets(tmin, tmax, output_cb=None):
    """ find a number of happy tickets in min..max range (inclusive) """
    result = 0
    for num in range(tmin, tmax + 1):
        left = num // 1000
        right = num % 1000
        if (sum_digits(left) == sum_digits(right)):
            result+=1
            if (output_cb):
                output_cb(num)
    return result

if __name__ == "__main__":
    tmin, tmax = map(int, str.split(input("Enter min and max, separated by space: ")))
    result = count_happy_tickets(tmin, tmax, print)
    print("Number of happy tickets in {}..{} range: {}".format(tmin, tmax, result))
