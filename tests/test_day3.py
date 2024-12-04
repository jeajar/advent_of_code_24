import pytest
from day3 import recover_memory, recover_memory_conditional


def test_recover_memory():
    """
    Test the function recover_memory can scan for mul(x,y) in corrupted data and return the sum of the products
    """

    test_data = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    expected_result = 161
    assert recover_memory(test_data) == expected_result


def test_recover_memory_conditional():
    """
    Test the function recover_memory can scan for mul(x,y) in corrupted data and return the sum of the products
    """

    test_data = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    expected_result = 48
    assert recover_memory_conditional(test_data) == expected_result


if __name__ == "__main__":
    pytest.main()
