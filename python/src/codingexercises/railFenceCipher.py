def encode(plain_text: str, rails: int) -> str:
    """
    Encodes the given plain text using the Rail Fence Cipher.

    The Rail Fence Cipher writes the message in a zigzag pattern along
    a set number of rails, then reads the message row by row.

    Args:
        plain_text: The text to be encoded.
        rails: The number of rails to use for the cipher.

    Returns:
        The encoded cipher text.

    Example:
        >>> encode("WEAREDISCOVEREDFLEEATONCE", 3)
        'WECRLTEERDSOEEFEAOCAIVDEN'
    """
    if rails == 1:
        return plain_text

    # Create a list of rails, each rail is a list of characters
    rail_strings: list[list[str]] = [[] for _ in range(rails)]
    current_rail = 0
    direction = 1  # 1 for down, -1 for up

    for char in plain_text:
        rail_strings[current_rail].append(char)
        current_rail += direction

        # Change direction if we've hit the top or bottom rail
        if current_rail == 0 or current_rail == rails - 1:
            direction *= -1

    # Concatenate all rails to form the cipher text
    cipher_text = "".join(["".join(rail) for rail in rail_strings])

    return cipher_text


def decode(cipher_text: str, rails: int) -> str:
    """
    Decodes the given cipher text using the Rail Fence Cipher.

    Reconstructs the original message by determining the original
    zigzag pattern and placing characters from the cipher text
    in their correct positions.

    Args:
        cipher_text: The text to be decoded.
        rails: The number of rails used in the encoding.

    Returns:
        The decoded plain text.

    Example:
        >>> decode('WECRLTEERDSOEEFEAOCAIVDEN', 3)
        'WEAREDISCOVEREDFLEEATONCE'
    """
    if rails == 1:
        return cipher_text

    # Create a list to represent the rail pattern
    pattern: list[int] = []
    current_rail = 0
    direction = 1

    # First, determine the pattern (which rail each character belongs to)
    for _ in range(len(cipher_text)):
        pattern.append(current_rail)
        current_rail += direction

        if current_rail == 0 or current_rail == rails - 1:
            direction *= -1

    # Now, split the cipher text into rails based on the pattern
    rail_indices: list[list[int]] = [[] for _ in range(rails)]

    # For each rail, collect the indices where it occurs in the pattern
    for index, rail in enumerate(pattern):
        rail_indices[rail].append(index)

    # Reconstruct the original plain text
    plain_text = [""] * len(cipher_text)
    pos = 0

    for rail in range(rails):
        for index in rail_indices[rail]:
            plain_text[index] = cipher_text[pos]
            pos += 1

    return "".join(plain_text)
