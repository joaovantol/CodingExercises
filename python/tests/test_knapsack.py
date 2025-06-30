from codingexercises.knapsack import maximumValue, maximumValueComb

def test_no_item() -> None:
    items: list = []

    assert maximumValue(10, items) == 0

def test_1_item_too_heavy() -> None:
    items = [
        {"weight": 100, "value": 1}
    ]

    assert maximumValue(10, items) == 0

def test_example() -> None:
    items = [
        {"weight": 5, "value": 10},
        {"weight": 4, "value": 40},
        {"weight": 6, "value": 30},
        {"weight": 4, "value": 50}
    ]

    assert maximumValue(10, items)== 90

def test_5_items_cannot_be_greedy_by_weight() -> None:
    items = [
        {"weight": 2, "value": 5},
        {"weight": 2, "value": 5},
        {"weight": 2, "value": 5},
        {"weight": 2, "value": 5},
        {"weight": 10, "value": 21}
    ]

    assert maximumValue(10, items)== 21

def test_5_items_cannot_be_greedy_by_value() -> None:
    items = [
        {"weight": 2, "value": 20},
        {"weight": 2, "value": 20},
        {"weight": 2, "value": 20},
        {"weight": 2, "value": 20},
        {"weight": 10, "value": 50}
    ]

    assert maximumValue(10, items)== 80

def test_8_items() -> None:
    items = [
        {"weight": 25, "value": 350},
        {"weight": 35, "value": 400},
        {"weight": 45, "value": 450},
        {"weight": 5, "value": 20},
        {"weight": 25, "value": 70},
        {"weight": 3, "value": 8},
        {"weight": 2, "value": 5},
        {"weight": 2, "value": 5}
    ]

    assert maximumValue(104, items)== 900

def test_15_items() -> None:
    items = [
        {"weight": 70, "value": 135},
        {"weight": 73, "value": 139},
        {"weight": 77, "value": 149},
        {"weight": 80, "value": 150},
        {"weight": 82, "value": 156},
        {"weight": 87, "value": 163},
        {"weight": 90, "value": 173},
        {"weight": 94, "value": 184},
        {"weight": 98, "value": 192},
        {"weight": 106, "value": 201},
        {"weight": 110, "value": 210},
        {"weight": 113, "value": 214},
        {"weight": 115, "value": 221},
        {"weight": 118, "value": 229},
        {"weight": 120, "value": 240}
    ]

    assert maximumValue(750, items)== 1458

def test_no_item2() -> None:
    items: list = []

    assert maximumValueComb(10, items) == 0

def test_1_item_too_heavy2() -> None:
    items = [
        {"weight": 100, "value": 1}
    ]

    assert maximumValueComb(10, items) == 0

def test_example2() -> None:
    items = [
        {"weight": 5, "value": 10},
        {"weight": 4, "value": 40},
        {"weight": 6, "value": 30},
        {"weight": 4, "value": 50}
    ]

    assert maximumValueComb(10, items)== 90

def test_5_items_cannot_be_greedy_by_weight2() -> None:
    items = [
        {"weight": 2, "value": 5},
        {"weight": 2, "value": 5},
        {"weight": 2, "value": 5},
        {"weight": 2, "value": 5},
        {"weight": 10, "value": 21}
    ]

    assert maximumValueComb(10, items)== 21

def test_5_items_cannot_be_greedy_by_value2() -> None:
    items = [
        {"weight": 2, "value": 20},
        {"weight": 2, "value": 20},
        {"weight": 2, "value": 20},
        {"weight": 2, "value": 20},
        {"weight": 10, "value": 50}
    ]

    assert maximumValueComb(10, items)== 80

def test_8_items2() -> None:
    items = [
        {"weight": 25, "value": 350},
        {"weight": 35, "value": 400},
        {"weight": 45, "value": 450},
        {"weight": 5, "value": 20},
        {"weight": 25, "value": 70},
        {"weight": 3, "value": 8},
        {"weight": 2, "value": 5},
        {"weight": 2, "value": 5}
    ]

    assert maximumValueComb(104, items)== 900

def test_15_items2() -> None:
    items = [
        {"weight": 70, "value": 135},
        {"weight": 73, "value": 139},
        {"weight": 77, "value": 149},
        {"weight": 80, "value": 150},
        {"weight": 82, "value": 156},
        {"weight": 87, "value": 163},
        {"weight": 90, "value": 173},
        {"weight": 94, "value": 184},
        {"weight": 98, "value": 192},
        {"weight": 106, "value": 201},
        {"weight": 110, "value": 210},
        {"weight": 113, "value": 214},
        {"weight": 115, "value": 221},
        {"weight": 118, "value": 229},
        {"weight": 120, "value": 240}
    ]

    assert maximumValueComb(750, items)== 1458
