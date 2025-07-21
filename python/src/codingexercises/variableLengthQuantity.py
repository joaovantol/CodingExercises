def encode(numbers: list) -> list:
    """
    Encode a list of numbers into a VLQ byte sequence.

    Variable Length Quantity (VLQ) is a method for storing integers in a variable number of bytes.
    Each byte uses the 7 least significant bits for the value and the most significant bit as a
    continuation flag (1 if more bytes follow, 0 if this is the last byte).

    Args:
        numbers: List of integers to be encoded.

    Returns:
        List of bytes representing the VLQ encoded numbers.

    Examples:
        >>> encode([0x7f])
        [127]
        >>> encode([0x4000])
        [129, 128, 0]
    """
    encoded_bytes = []
    for number in numbers:
        # Handle 0 case immediately
        if number == 0:
            encoded_bytes.append(0)
            continue

        # Process each 7-bit chunk
        chunks = []
        while number > 0:
            chunk = number & 0x7f  # Get the least significant 7 bits
            number >>= 7           # Right shift by 7 bits
            chunks.append(chunk)

        # Set the continuation bit on all chunks except the last one
        for i in range(len(chunks) - 1):
            chunks[i] |= 0x80

        # Add chunks in little-endian order (least significant byte first)
        encoded_bytes.extend(reversed(chunks))

    return encoded_bytes


def decode(bytes_: list) -> list:
    """
    Decode a VLQ byte sequence into a list of numbers.

    Args:
        bytes_: List of bytes representing VLQ encoded numbers.

    Returns:
        List of decoded integers.

    Raises:
        ValueError: If the input ends with an incomplete sequence (continuation bit set on last byte).

    Examples:
        >>> decode([0x7f])
        [127]
        >>> decode([0x81, 0x80, 0x00])
        [16384]
    """
    numbers = []
    current_number = 0

    for byte in bytes_:
        # Add the 7 bits to the current number
        current_number = (current_number << 7) | (byte & 0x7f)

        # Check if this is the last byte of the number
        if not (byte & 0x80):
            numbers.append(current_number)
            current_number = 0

    # If we have a remaining current_number, the input was incomplete
    if current_number != 0:
        raise ValueError("incomplete sequence")

    return numbers