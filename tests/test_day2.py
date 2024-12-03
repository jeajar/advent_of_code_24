import pytest

from day2 import report_is_safe, safe_with_dampener


def test_report_is_safe():
    test_data = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]

    expected_results = [True, False, False, False, False, True]

    for line, expected in zip(test_data, expected_results):
        assert report_is_safe(line) == expected


def test_report_is_safe_with_dampener():
    test_data = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]

    expected_results = [True, False, False, True, True, True]

    for line, expected in zip(test_data, expected_results):
        assert safe_with_dampener(line) == expected


if __name__ == "__main__":
    pytest.main()
