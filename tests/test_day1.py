import pytest
from day1 import caluculate_distance, calculate_similarity_score


def test_caluculate_distance():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    expected_distance = 11  # Excpected distance is 11, from the example
    assert caluculate_distance(list1, list2) == expected_distance

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    expected_distance = 9
    assert caluculate_distance(list1, list2) == expected_distance

    list1 = [10, 20, 30]
    list2 = [15, 25, 35]
    expected_distance = 15
    assert caluculate_distance(list1, list2) == expected_distance

    list1 = [1, 1, 1]
    list2 = [1, 1, 1]
    expected_distance = 0
    assert caluculate_distance(list1, list2) == expected_distance


def test_calculate_similarity_score():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    expected_score = 31
    assert calculate_similarity_score(list1, list2) == expected_score

    list1 = []
    list2 = []
    expected_score = 0
    assert calculate_similarity_score(list1, list2) == expected_score


if __name__ == "__main__":
    pytest.main()
