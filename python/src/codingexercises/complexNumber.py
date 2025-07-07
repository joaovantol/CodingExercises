from math import sqrt, exp, cos, sin
from typing import Any

class ComplexNumber:
    """
    A class representing complex numbers with real and imaginary parts.
    Supports basic arithmetic operations and common complex number functions.
    """

    def __init__(self, real: int | float, imaginary: int | float) -> None:
        """
        Initialize a complex number with given real and imaginary parts.

        :param real: The real part of the complex number
        :param imaginary: The imaginary part of the complex number
        """
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: Any) -> bool:
        """
        Check equality between two complex numbers.

        :param other: Another complex number to compare with
        :return: True if both numbers have equal real and imaginary parts
        """
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return self.real == other.real and self.imaginary == other.imaginary

    def __repr__(self) -> str:
        """
        Return a formal string representation of the complex number.
        """
        return f"ComplexNumber({self.real}, {self.imaginary})"

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the complex number.
        """
        return f"{self.real}{self.imaginary:+}i"

    def __add__(self, other: Any) -> "ComplexNumber":
        """
        Add two complex numbers or a complex number with a real number.

        :param other: Another complex number or real number
        :return: New complex number representing the sum
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real + other.real,
                self.imaginary + other.imaginary
            )
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)
        else:
            return NotImplemented

    def __radd__(self, other: Any) -> "ComplexNumber":
        """
        Handle reflected addition for cases like real + complex.
        """
        return self.__add__(other)

    def __sub__(self, other: Any) -> "ComplexNumber":
        """
        Subtract two complex numbers or a real number from a complex number.

        :param other: Another complex number or real number
        :return: New complex number representing the difference
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real - other.real,
                self.imaginary - other.imaginary
            )
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imaginary)
        else:
            return NotImplemented

    def __rsub__(self, other: Any) -> "ComplexNumber":
        """
        Handle reflected subtraction for cases like real - complex.
        """
        if isinstance(other, (int, float)):
            return ComplexNumber(other - self.real, -self.imaginary)
        else:
            return NotImplemented

    def __mul__(self, other: Any) -> "ComplexNumber":
        """
        Multiply two complex numbers or a complex number with a real number.

        :param other: Another complex number or real number
        :return: New complex number representing the product
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real
            )
        elif isinstance(other, (int, float)):
            return ComplexNumber(
                self.real * other,
                self.imaginary * other
            )
        else:
            return NotImplemented

    def __rmul__(self, other: Any) -> "ComplexNumber":
        """
        Handle reflected multiplication for cases like real * complex.
        """
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> "ComplexNumber":
        """
        Divide two complex numbers or a complex number by a real number.

        :param other: Another complex number or real number
        :return: New complex number representing the quotient
        """
        if isinstance(other, ComplexNumber):
            denominator = other.real**2 + other.imaginary**2
            return ComplexNumber(
                (self.real * other.real + self.imaginary * other.imaginary) / denominator,
                (self.imaginary * other.real - self.real * other.imaginary) / denominator
            )
        elif isinstance(other, (int, float)):
            return ComplexNumber(
                self.real / other,
                self.imaginary / other
            )
        else:
            return NotImplemented

    def __rtruediv__(self, other: Any) -> "ComplexNumber":
        """
        Handle reflected division for cases like real / complex.
        """
        if isinstance(other, (int, float)):
            denominator = self.real**2 + self.imaginary**2
            return ComplexNumber(
                (other * self.real) / denominator,
                (-other * self.imaginary) / denominator
            )
        else:
            return NotImplemented

    def __abs__(self) -> Any:
        """
        Calculate the magnitude (absolute value) of the complex number.

        :return: The magnitude as a float
        """
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self) -> "ComplexNumber":
        """
        Return the complex conjugate of the number.

        :return: New complex number representing the conjugate
        """
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self) -> "ComplexNumber":
        """
        Calculate the exponential of the complex number (e^z).

        :return: New complex number representing e^z
        """
        exp_real = exp(self.real)
        return ComplexNumber(
            exp_real * cos(self.imaginary),
            exp_real * sin(self.imaginary)
        )