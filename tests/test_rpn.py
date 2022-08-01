from lib.RPN import RPN
import pytest

calculator = RPN()


@pytest.mark.parametrize("cli, result", [
    ("6 3 /", 2),
    ("2 3 *", 6),
    ("2 3 +", 5),
    ("2 3 -", -1),
    ("4 3 %", 1),
    ("2 3 * 5 + 2 / 2 - 1 -", 2),
    ("2 3 3 * 5 /", 1),
    ("2 2 * 2 10 *", 20),
    ("4 4 4 * *", 64),
    ("123 456 +", 579)
])
def test_acceptance(cli, result):
    assert calculator.calculate(cli) == result


@pytest.mark.parametrize("cli", [
    "6 0 /",
])
def test_zero_division(cli):
    with pytest.raises(ZeroDivisionError):
        calculator.calculate(cli)


@pytest.mark.parametrize("cli", [
    "A B /",
    "> < /",
    "TRUE FALSE /",
    "SELECT * FROM Users",  # Sql inject
    "#########",  # Multiple sequential non number value
    " ",  # Space
    " ",  # Indent
    "",  # Empty input
    "2^2 2 +",  # Squaring
    "(2 2 *) 3 + "
])
def test_destructive(cli):
    with pytest.raises(ValueError):
        calculator.calculate(cli)
