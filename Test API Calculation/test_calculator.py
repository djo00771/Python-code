import pytest
from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

# Позитивные тесты
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_devizion_calculate_correctly(self):
        assert self.calc.divizion(self, 6, 2) == 3

    def test_substraction_calculate_correctly(self):
        assert self.calc.substraction(self, 5, 3) == 2

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 5) == 10

# Негативные тесты
#     def test_multiply_calculate_filed(self):
#         assert self.calc.multiply(self, 2, 2) == 5
#
#     def test_devizion_calculate_filed(self):
#         assert self.calc.divizion(self, 6, 2) == 2
#
#     def test_substraction_calculate_filed(self):
#         assert self.calc.substraction(self, 5, 3) == 3
#
#     def test_adding_calculate_filed(self):
#         assert self.calc.adding(self, 5, 5) == 11
