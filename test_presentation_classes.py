# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# SaimaAhmed,2023-11-30,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee


class TestIO(unittest.TestCase):
    def test_input_menu_choice(self):
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice("test")
            self.assertEqual('2', choice)

    def test_input_employee_data(self):
        with patch('builtins.input', side_effect=['Vic', 'Vu', '2023-11-30', 2]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees,employee_type= Employee)
            self.assertEqual(1, len(employees))
            self.assertEqual('Vic', employees[0].first_name)
            self.assertEqual('Vu', employees[0].last_name)
            self.assertEqual('2023-11-30', employees[0].review_date)
            self.assertEqual(2, employees[0].review_rating)

    def test_input_employee_data_invalid_review_date_format(self):
        with patch('builtins.input', side_effect=['Vic', 'Vu', '11-30-2023', 2]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees,employee_type = Employee)
            self.assertEqual(0, len(employees))

    if __name__ == '__main__':
        unittest.main()
