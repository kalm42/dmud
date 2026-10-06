def travel_seconds(length_mm: int, speed_mm_per_second: int) -> int:
    """Time to complete one travel segment, rounded up to a whole second (GDD G04).

    Integer ceiling division avoids binary-float misrounding such as 7 / 1.4. For
    example, travel_seconds(7000, 1400) == 5 and travel_seconds(7000, 2800) == 3.
    """
    return -(-length_mm // speed_mm_per_second)
