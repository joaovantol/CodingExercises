def kangaroo(
    kanga1: float,
    speed1: float,
    kanga2: float,
    speed2: float,
) -> bool:
    """
    Determine if two kangaroos will meet at the same position at the same time.

    Args:
        kanga1: Starting position of kangaroo 1
        speed1: Jump distance of kangaroo 1
        kanga2: Starting position of kangaroo 2
        speed2: Jump distance of kangaroo 2

    Returns:
        True if they will meet, False otherwise
    """
    if speed1 == speed2:
        return kanga1 == kanga2
    jumps = (kanga2 - kanga1) / (speed1 - speed2)

    return jumps >= 0 and jumps.is_integer()
