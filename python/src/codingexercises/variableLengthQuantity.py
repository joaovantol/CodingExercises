def convertToBaseN(number: int, base: int) -> list[int]:
    """
    Convert a decimal number to a specified base representation.

    Args:
        number: The positive integer to convert (must be >= 0)
        base: The target base

    Returns:
        A list representation of the number in the specified base

    Examples:
        >>> to_base_n(5, 2)
        [1, 0, 1]
        >>> to_base_n(255, 128)
        [1, 127]
        >>> to_base_n(0xFF, 128)
        [1, 127]
    """
    if not number:
        return [0]

    values = []
    while number > 0:
        values.append(number%base)
        number = number//base

    return values[::-1]

def encode(numbers: list[int]) -> list[int]:
    """
    Encode a list of numbers into a VLQ byte sequence.

    Variable Length Quantity (VLQ) is a method for storing integers in a
    variable number of bytes. Each byte uses the 7 least significant bits for
    the value and the most significant bit as a continuation flag (1 if more
    bytes follow, 0 if this is the last byte).

    Args:
        numbers: List of integers to be encoded.

    Returns:
        List of bytes representing the VLQ encoded numbers.

    Examples:
        >>> encode([0x7F])
        [127]
        >>> encode([0x4000])
        [129, 128, 0]
    """
    encoded = []

    for n in numbers:
        base128 = convertToBaseN(n, 128)
        encoded += [byte_ + 128 for byte_ in base128[:-1]] + [base128[-1]]

    return encoded

def decode(bytes_: list[int]) -> list[int]:
    """
    Decode a VLQ byte sequence into a list of numbers.

    Args:
        bytes_: List of bytes representing VLQ encoded numbers.

    Returns:
        List of decoded integers.

    Raises:
        ValueError: If the input ends with an incomplete sequence (continuation
        bit set on last byte).

    Examples:
        >>> decode([0x7F])
        [127]
        >>> decode([0x81, 0x80, 0x00])
        [16384]
    """
    decoded = []
    number = 0

    for byte in bytes_:
        number *= 128
        number += (byte%128)
        if byte < 128:
            decoded.append(number)
            number = 0

    if number > 0 or 0 == len(decoded):
        raise ValueError("incomplete sequence")

    return decoded