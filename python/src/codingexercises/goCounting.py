from collections import defaultdict
from itertools import product
from typing import Any

WHITE = "W"
BLACK = "B"
NONE = " "
STONES = {WHITE, BLACK, NONE}
DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Board:
    """
    A class representing a go board.
    Supports territory counting operations.
    """

    def __init__(self, board: list[str]) -> None:
        self.rows = board
        self.columns = list(zip(*board))

    def onboard(self, x: int, y: int) -> bool:
        """
        Check if the the a pair (x, y) representing a row and a column exists
        on the board.

        Args:
            x: The row number.
            y: The column number.

        Returns:
            Boolean.
        """
        return 0 <= x < len(self.columns) and 0 <= y < len(self.rows)

    def territory(self, x: int, y: int) -> tuple[Any, set[Any]]:
        """
        Calculates the territory surrounding a given pair of coordinates.

        Args:
            x: The row number.
            y: The column number.

        Returns:
            A tuple containing a territory belonging to black, white or none.
        """
        if not self.onboard(x, y):
            raise ValueError("Invalid coordinate")

        stack = [(x, y)]
        territory: set[Any] = set()
        stones: set[Any] = set()

        while stack:
            x, y = stack.pop()
            if (x, y) not in territory and self.onboard(x, y):
                stone = self.columns[x][y]
                if stone == NONE:
                    territory.add((x, y))
                    stack += [(x + dx, y + dy) for dx, dy in DELTAS]
                else:
                    stones.add(stone)

        if len(stones) == 1 and len(territory) > 0:
            return (stones.pop(), territory)
        return (NONE, territory)

    def territories(self) -> dict[str, set[Any] | None]:
        """
        Calculates all territories in a go board.

        Returns:
            A dictionary containing all territories belonging to black, white
            and none.
        """
        territories: defaultdict[str, set[Any]] = defaultdict(set)

        for x, y in product(range(0, len(self.columns)), range(0, len(self.rows))):
            stone, territory = self.territory(x, y)
            territories[stone] |= territory

        return {
            stone: territories.get(stone) if territories.get(stone) else set()
            for stone in STONES
        }
