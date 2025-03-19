import pytest
from src.functions import divide  # Adjust this import based on your module name

# Happy Path Tests
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (7.5, 2.5, 3),
        (-6, 2, -3),
        (0, 5, 0),
    ],
)
def test_divide_happy(a, b, expected):
    """Tests valid division cases."""
    assert divide(a, b) == expected

# Sad Path Tests
@pytest.mark.parametrize(
    "a, b, expected_exception, expected_message",
    [
        (10, 0, ValueError, "Cannot divide by zero"),  # Zero division
        ("10", 2, TypeError, "Both arguments must be numbers"),  # Invalid type
        (10, "2", TypeError, "Both arguments must be numbers"),  # Invalid type
        (None, 5, TypeError, "Both arguments must be numbers"),  # NoneType
    ],
)
def test_divide_sad(a, b, expected_exception, expected_message):
    """Tests invalid inputs and exception handling."""
    with pytest.raises(expected_exception) as exc_info:
        divide(a, b)
    assert str(exc_info.value) == expected_message
