import pytest

from service.function_service import suma

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (2, 3, 5),
        (4, 5, 9)
    ]
)
def test_suma(num1, num2, expected):
    assert suma(num1, num2) == expected