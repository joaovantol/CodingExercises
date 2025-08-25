from codingexercises.redundantSignalTowers import redundant_towers


def test_code_wars_example() -> None:
    assert redundant_towers([1, 2, 4], [1, 1, 3]) == 1


def test_code_wars_example_minus_tower_2() -> None:
    assert redundant_towers([1, 4], [1, 3]) == 0


def test_3() -> None:
    assert redundant_towers([1, 2], [3, 2]) == 1


def test_4() -> None:
    assert redundant_towers([1, 2], [2, 1]) == 1


def test_5() -> None:
    assert redundant_towers([1, 2], [2, 3]) == 1


def test_6() -> None:
    assert redundant_towers([0, 3, 5], [2, 1, 3]) == 1


def test_7() -> None:
    assert redundant_towers([0, 4], [6, 1]) == 1
