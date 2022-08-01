from lib.RPN import RPN
import pytest

calculator = RPN()


@pytest.mark.parametrize("cli, result", [
    (r"6 3 /", 2),
    (r"2 3 *", 6),
    (r"2 3 +", 5),
    (r"2 3 -", -1),
    (r"4 3 %", 1),
    (r"2 3 * 5 + 2 / 2 - 1 -", 2),
    (r"2 3 3 * 5 /", 1),
    (r"2 2 * 2 10 *", 20),
    (r"4 4 4 * *", 64),
])
def test_acceptance(cli, result):
    assert calculator.calculate(cli) == result


@pytest.mark.parametrize("cli", [
    r"6 0 /",
])
def test_zero_division(cli):
    with pytest.raises(ZeroDivisionError):
        calculator.calculate(cli)


@pytest.mark.parametrize("cli", [
    r"A B /",
    r"> < /",
    r"TRUE FALSE /",
    r"SELECT * FROM Users",  # Sql inject
    r"#########",  # Multiple sequential non number value
    r" ",  # Space
    r" ",  # Indent
    r"",  # Empty input
    r"",
])
def test_destructive(cli):
    with pytest.raises(ValueError):
        calculator.calculate(cli)
