class Board:
    """Represents a Go board and handles territory counting.

    The Board class manages the state of a Go game board and provides methods
    to determine the territories controlled by each player (Black, White)
    and neutral points.

    Attributes:
        board (list): 2D list representing the board state
        width (int): Number of columns in the board
        height (int): Number of rows in the board
    """

    def __init__(self, board):
        """Initialize a new Board instance.

        Args:
            board (list of str): List of strings representing the board rows.
                                 'B' represents Black stone, 'W' represents
                                 White stone, ' ' represents empty point.
        """
        self.board = [list(row) for row in board]
        self.height = len(board)
        self.width = len(board[0]) if self.height > 0 else 0

    def get_territory(self, x, y):
        """Find the territory connected to a given coordinate.

        A territory consists of all connected empty points that are completely
        surrounded by stones of the same color (or the board edge).

        Args:
            x (int): Column coordinate (0-based)
            y (int): Row coordinate (0-based)

        Returns:
            tuple: (set of coordinates, owner) where owner is:
                   'BLACK' if territory is surrounded by Black stones
                   'WHITE' if territory is surrounded by White stones
                   'NONE' if territory has mixed boundaries or no boundaries

        Raises:
            ValueError: If coordinates are invalid
        """
        # Validate coordinates
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError("Invalid coordinate")

        # If the point is not empty, it's not a territory
        if self.board[y][x] != " ":
            return set(), "NONE"

        # Use BFS to find all connected empty points
        visited = set()
        territory = set()
        queue = [(x, y)]
        boundaries = set()

        while queue:
            cx, cy = queue.pop(0)
            if (cx, cy) in visited:
                continue

            visited.add((cx, cy))
            territory.add((cx, cy))

            # Check all four neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = cx + dx, cy + dy

                # Check if neighbor is within bounds
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbor = self.board[ny][nx]
                    if neighbor == " ":
                        if (nx, ny) not in visited:
                            queue.append((nx, ny))
                    else:
                        boundaries.add(neighbor)
                else:
                    # Edge of board counts as a boundary
                    boundaries.add("EDGE")

        # Determine territory owner
        if "B" in boundaries and "W" not in boundaries and "EDGE" not in boundaries:
            owner = "BLACK"
        elif "W" in boundaries and "B" not in boundaries and "EDGE" not in boundaries:
            owner = "WHITE"
        else:
            owner = "NONE"

        return territory, owner

    def territories(self):
        """Calculate all territories on the board.

        Returns:
            dict: A dictionary with keys 'BLACK', 'WHITE', 'NONE' mapping
                  to sets of coordinates controlled by each.
        """
        all_territories = {"BLACK": set(), "WHITE": set(), "NONE": set()}
        visited = set()

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == " " and (x, y) not in visited:
                    territory, owner = self.get_territory(x, y)
                    all_territories[owner] |= territory
                    visited |= territory

        return all_territories


def main():
    """Example usage of the Board class."""
    board = ["  B  ", " B B ", "B W B", " B B ", "  B  "]

    go_board = Board(board)
    territories = go_board.territories()

    print("Black territories:", territories["BLACK"])
    print("White territories:", territories["WHITE"])
    print("Neutral territories:", territories["NONE"])


if __name__ == "__main__":
    main()
