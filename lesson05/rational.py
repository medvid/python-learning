import number_theory

class Rational:
    def __init__(self, x, y):
        gcd = number_theory.gcd(x, y)
        self.x = x // gcd
        self.y = y // gcd

    def from_str(string):
        x, y = map(int, string.split('/'))
        return Rational(x, y)

    def __str__(self):
        return "{}/{}".format(self.x, self.y)

    def __repr__(self):
        return __str__(self)

    def add(self, r):
        return Rational(self.x * r.y + self.y * r.x, self.y * r.y)

    def sub(self, r):
        return Rational(self.x * r.y - self.y * r.x, self.y * r.y)

    def mul(self, r):
        return Rational(self.x * r.x, self.y * r.y)

    def div(self, r):
        return Rational(self.x * r.y, self.y * r.x)

if __name__ == "__main__":
    r1_1 = Rational(1, 1)
    r2_3 = Rational(2, 3)
    print(r2_3.add(r2_3))
    print(r2_3.add(r2_3).add(r2_3))
