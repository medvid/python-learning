def min(x, y):
    return x if x < y else y

def gcd(x, y):
    result = 1
    div = 1
    while True:
        if (x % div == 0) and (y % div == 0):
            result *= div
            x //= div
            y //= div
            div = 1
        if div > min(x, y):
            break
        div += 1
    return result

def lcm(x, y):
    return x * y / gcd(x, y)
