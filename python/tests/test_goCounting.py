from typing import Any

from pytest import raises

from codingexercises.goCounting import BLACK, NONE, WHITE, Board


def test_black_corner_territory_on_5x5_board() -> None:
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
    stone, territory = board.territory(x=0, y=1)

    expected_stone = BLACK
    expected_territory = {(0, 0), (0, 1), (1, 0)}

    assert expected_stone == stone
    assert expected_territory == territory


def test_white_center_territory_on_5x5_board() -> None:
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
    stone, territory = board.territory(x=2, y=3)

    expected_stone = WHITE
    expected_territory = {(2, 3)}

    assert expected_stone == stone
    assert expected_territory == territory


def test_open_corner_territory_on_5x5_board() -> None:
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
    stone, territory = board.territory(x=1, y=4)

    expected_stone = NONE
    expected_territory = {(0, 3), (0, 4), (1, 4)}

    assert expected_stone == stone
    assert expected_territory == territory


def test_a_stone_and_not_a_territory_on_5x5_board() -> None:
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
    stone, territory = board.territory(x=1, y=1)

    expected_stone = NONE
    expected_territory: set[Any] = set()

    assert expected_stone == stone
    assert expected_territory == territory


def test_invalid_because_x_is_too_low_for_5x5_board() -> None:
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])

    with raises(ValueError, match="Invalid coordinate"):
        board.territory(x=-1, y=1)


def test_invalid_because_x_is_too_high_for_5x5_board() -> None:
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])

    with raises(ValueError, match="Invalid coordinate"):
        board.territory(x=5, y=1)


def test_invalid_because_y_is_too_low_for_5x5_board() -> None:
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])

    with raises(ValueError, match="Invalid coordinate"):
        board.territory(x=1, y=-1)


def test_invalid_because_y_is_too_high_for_5x5_board() -> None:
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])

    with raises(ValueError, match="Invalid coordinate"):
        board.territory(x=1, y=5)


def test_one_territory_is_the_whole_board() -> None:
    board = Board([" "])
    territories = board.territories()

    expected_black_territory: set[Any] = set()
    expected_white_territory: set[Any] = set()
    expected_none_territory = {(0, 0)}

    assert expected_black_territory == territories[BLACK]
    assert expected_white_territory == territories[WHITE]
    assert expected_none_territory == territories[NONE]


def test_two_territory_rectangular_board() -> None:
    board = Board([" BW ", " BW "])
    territories = board.territories()

    expected_black_territory = {(0, 0), (0, 1)}
    expected_white_territory = {(3, 0), (3, 1)}
    expected_none_territory: set[Any] = set()

    assert expected_black_territory == territories[BLACK]
    assert expected_white_territory == territories[WHITE]
    assert expected_none_territory == territories[NONE]


def test_two_region_rectangular_board() -> None:
    board = Board([" B "])
    territories = board.territories()

    expected_black_territory = {(0, 0), (2, 0)}
    expected_white_territory: set[Any] = set()
    expected_none_territory: set[Any] = set()

    assert expected_black_territory == territories[BLACK]
    assert expected_white_territory == territories[WHITE]
    assert expected_none_territory == territories[NONE]
