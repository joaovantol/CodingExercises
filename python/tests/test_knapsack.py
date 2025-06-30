from codingexercises.knapsack import maximum_value

def test_1() -> None:
    items = [
        {"weight": 5, "value": 10},
        {"weight": 4, "value": 40},
        {"weight": 6, "value": 30},
        {"weight": 4, "value": 50}
    ]

    assert maximum_value (10, items )== 90