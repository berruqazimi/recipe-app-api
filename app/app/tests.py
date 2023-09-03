"""Simple Tests"""

from django.test import SimpleTestCase

from app import calc

class ClacTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding mthod numbers"""
        res = calc.Calculator(5,6)
        self.assertEqual(res , 10)