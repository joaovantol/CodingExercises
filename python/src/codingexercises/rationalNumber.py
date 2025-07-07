import math


class Rational:
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        # Reduce to simplest form during initialization
        common_divisor = math.gcd(numerator, denominator)
        reduced_num = numerator // common_divisor
        reduced_den = denominator // common_divisor

        # Ensure denominator is positive
        if reduced_den < 0:
            reduced_num *= -1
            reduced_den *= -1

        self.numerator = reduced_num
        self.denominator = reduced_den

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = (self.numerator * other.denominator +
                   other.numerator * self.denominator)
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = (self.numerator * other.denominator -
                   other.numerator * self.denominator)
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Rational(new_num, new_den)

    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power: int):
        if not isinstance(power, int):
            return NotImplemented
        if power == 0:
            return Rational(1)
        if power > 0:
            return Rational(self.numerator ** power, self.denominator ** power)
        else:
            return Rational(self.denominator ** abs(power),
                           self.numerator ** abs(power))

    def __rpow__(self, base):
        if not isinstance(base, (int, float)):
            return NotImplemented
        return base ** (self.numerator / self.denominator)

    # Comparison operators
    def __lt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)

    def __le__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator * other.denominator <=
                other.numerator * self.denominator)

    def __gt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator * other.denominator >
                other.numerator * self.denominator)

    def __ge__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator * other.denominator >=
                other.numerator * self.denominator)

    # Unary operators
    def __pos__(self):
        return Rational(+self.numerator, self.denominator)

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)