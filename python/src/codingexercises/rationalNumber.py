import math
from typing import Any

class Rational:
    """A class representing rational numbers (fractions) with numerator and denominator.

    This class provides arithmetic operations, comparisons, and proper representation
    of rational numbers in their reduced form. All operations return new Rational
    instances rather than modifying the current object.

    Attributes:
        numerator (int): The numerator of the rational number (in reduced form)
        denominator (int): The denominator of the rational number (positive, in reduced form)
    """

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        """Initialize a Rational number with numerator and denominator.

        The fraction is automatically reduced to its simplest form, and the denominator
        is guaranteed to be positive. Raises ValueError for zero denominator.

        Args:
            numerator: The numerator of the fraction
            denominator: The denominator of the fraction (default is 1)

        Raises:
            ValueError: If denominator is zero
        """
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

    def __eq__(self, other: Any) -> bool:
        """Check equality between this Rational and another object.

        Args:
            other: The object to compare with

        Returns:
            bool: True if other is a Rational with same numerator and denominator,
                  False otherwise. Returns NotImplemented if other is not a Rational.
        """
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __repr__(self) -> str:
        """Return an unambiguous string representation of the Rational.

        Returns:
            str: The string representation that can be used to recreate the object
        """
        return f"Rational({self.numerator}, {self.denominator})"

    def __str__(self) -> str:
        """Return a user-friendly string representation of the Rational.

        Returns:
            str: The fraction in 'a/b' form, or just 'a' if denominator is 1
        """
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: Any) -> Any:
        """Add this Rational to another Rational or number.

        Args:
            other: The Rational or number to add

        Returns:
            Rational: The sum as a new Rational in reduced form
            NotImplemented: If other is not a Rational
        """
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = (self.numerator * other.denominator +
                   other.numerator * self.denominator)
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __sub__(self, other: Any) -> Any:
        """Subtract another Rational from this Rational.

        Args:
            other: The Rational to subtract

        Returns:
            Rational: The difference as a new Rational in reduced form
            NotImplemented: If other is not a Rational
        """
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = (self.numerator * other.denominator -
                   other.numerator * self.denominator)
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __mul__(self, other: Any) -> Any:
        """Multiply this Rational by another Rational.

        Args:
            other: The Rational to multiply by

        Returns:
            Rational: The product as a new Rational in reduced form
            NotImplemented: If other is not a Rational
        """
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __truediv__(self, other: Any) -> Any:
        """Divide this Rational by another Rational.

        Args:
            other: The Rational to divide by

        Returns:
            Rational: The quotient as a new Rational in reduced form
            NotImplemented: If other is not a Rational

        Raises:
            ZeroDivisionError: If other is zero
        """
        if not isinstance(other, Rational):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Rational(new_num, new_den)

    def __abs__(self) -> Any:
        """Return the absolute value of this Rational.

        Returns:
            Rational: A new Rational with positive numerator and denominator
        """
        return Rational(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power: int) -> Any:
        """Raise this Rational to an integer power.

        Args:
            power: The integer exponent (can be positive, negative, or zero)

        Returns:
            Rational: The result of exponentiation as a new Rational
            NotImplemented: If power is not an integer
        """
        if not isinstance(power, int):
            return NotImplemented
        if power == 0:
            return Rational(1)
        if power > 0:
            return Rational(self.numerator ** power, self.denominator ** power)
        else:
            return Rational(self.denominator ** abs(power),
                           self.numerator ** abs(power))

    def __rpow__(self, base: Any) -> float:
        """Raise a number to the power of this Rational (for float exponentiation).

        Implements the operation: base ** (self.numerator/self.denominator)

        Args:
            base: The number to raise to this Rational's power

        Returns:
            float: The result of the exponentiation
            NotImplemented: If base is not a number
        """
        if not isinstance(base, (int, float)):
            return NotImplemented
        return base ** (self.numerator / self.denominator)

    # Comparison operators
    def __lt__(self, other: Any) -> bool:
        """Check if this Rational is less than another Rational.

        Args:
            other: The Rational to compare with

        Returns:
            bool: True if this Rational is less than other
            NotImplemented: If other is not a Rational
        """
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)

    def __le__(self, other: Any) -> bool:
        """Check if this Rational is less than or equal to another Rational.

        Args:
            other: The Rational to compare with

        Returns:
            bool: True if this Rational is less than or equal to other
            NotImplemented: If other is not a Rational
        """
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator * other.denominator <=
                other.numerator * self.denominator)

    def __gt__(self, other: Any) -> bool:
        """Check if this Rational is greater than another Rational.

        Args:
            other: The Rational to compare with

        Returns:
            bool: True if this Rational is greater than other
            NotImplemented: If other is not a Rational
        """
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator * other.denominator >
                other.numerator * self.denominator)

    def __ge__(self, other: Any) -> bool:
        """Check if this Rational is greater than or equal to another Rational.

        Args:
            other: The Rational to compare with

        Returns:
            bool: True if this Rational is greater than or equal to other
            NotImplemented: If other is not a Rational
        """
        if not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator * other.denominator >=
                other.numerator * self.denominator)

    # Unary operators
    def __pos__(self) -> Any:
        """Return this Rational with positive sign (unary + operator).

        Returns:
            Rational: The same Rational (since it's already in reduced form)
        """
        return Rational(+self.numerator, self.denominator)

    def __neg__(self) -> Any:
        """Return the negation of this Rational (unary - operator).

        Returns:
            Rational: A new Rational with negated numerator
        """
        return Rational(-self.numerator, self.denominator)