import unittest
import math
from parameterized import parameterized
from app.main import Calculator
from app.error import InvalidInputException


class TestCalculatorLog(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    @parameterized.expand([
        ("log_base_2", 8, 2, 3),
        ("log_base_10", 100, 10, 2),
        ("log_base_e", math.e, math.e, 1),
        ("log_base_5", 25, 5, 2),
        ("log_small_base", 0.01, 10, -2),
    ])
    def test_log_valid_values(self, name, a, base, expected_result):
        actual_result = self.calc.log(a, base)
        self.assertAlmostEqual(actual_result, expected_result)

    @parameterized.expand([
        ("string_a", "abc", 2, TypeError),
        ("string_base", 10, "xyz", TypeError),
        ("none_a", None, 2, TypeError),
        ("none_base", 10, None, TypeError),
    ])
    def test_log_invalid_types(self, name, a, base, expected_exception):
        with self.assertRaises(expected_exception):
            self.calc.log(a, base)

    @parameterized.expand([
        ("zero_a", 0, 2, InvalidInputException),
        ("one_a", 1, 2, InvalidInputException),
        ("negative_a", -10, 2, InvalidInputException),
        ("zero_base", 10, 0, InvalidInputException),
        ("negative_base", 10, -5, InvalidInputException),
    ])
    def test_log_invalid_domain(self, name, a, base, expected_exception):
        with self.assertRaises(expected_exception):
            self.calc.log(a, base)


if __name__ == "__main__":
    unittest.main()
