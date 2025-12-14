from codingexercises.staircase import minimumCostDP, optimizedMinimumCostDP


def test_example_1() -> None:
    cost = [10, 15, 20]
    minCost = 15

    assert minimumCostDP(cost) == minCost
    assert optimizedMinimumCostDP(cost) == minCost


def test_example_2() -> None:
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    minCost = 6

    assert minimumCostDP(cost) == minCost
    assert optimizedMinimumCostDP(cost) == minCost


def test_example_3() -> None:
    cost = [16, 19, 10, 12, 18]
    minCost = 31

    assert minimumCostDP(cost) == minCost
    assert optimizedMinimumCostDP(cost) == minCost


def test_example_4() -> None:
    cost = [7]
    minCost = 7

    assert minimumCostDP(cost) == minCost
    assert optimizedMinimumCostDP(cost) == minCost


def test_example_5() -> None:
    cost = [44, 3]
    minCost = 3

    assert minimumCostDP(cost) == minCost
    assert optimizedMinimumCostDP(cost) == minCost


def test_example_6() -> None:
    cost = [3, 44]
    minCost = 3

    assert minimumCostDP(cost) == minCost
    assert optimizedMinimumCostDP(cost) == minCost
