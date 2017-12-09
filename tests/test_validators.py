import unittest

from yu.validators import ValueRangeValidator, ValidationError


class TestValueRangeValidator(unittest.TestCase):
    def setUp(self):
        self.validator = ValueRangeValidator(2, 5)

    def test_normal_value(self):
        self.validator(2)
        self.validator(3)
        self.validator(5)

    def test_less_than_min_value(self):
        with self.assertRaisesRegex(ValidationError, '过小.*'):
            self.validator(1)

    def test_great_than_max_value(self):
        with self.assertRaisesRegex(ValidationError, '过大.*'):
            self.validator(6)
