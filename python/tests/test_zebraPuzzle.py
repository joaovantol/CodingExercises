from pytest import raises
from codingexercises.zebraPuzzle import ZebraPuzzle

def test_solution_exists() -> None:
    puzzle = ZebraPuzzle()

    assert puzzle.solve() == True

def test_who_drinks_water() -> None:
    puzzle = ZebraPuzzle()
    puzzle.solve()

    assert puzzle.drinksWater() == "norwegian"

def test_who_owns_zebra() -> None:
    puzzle = ZebraPuzzle()
    puzzle.solve()

    assert puzzle.ownsZebra() == "japanese"
