# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# SaimaAhmed,2023-11-30,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person,Employee

class TestPerson(unittest.TestCase):

    def test_person_init(self):
        person = Person('Vic', 'Vu')
        self.assertEqual('Vic',person.first_name)
        self.assertEqual('Vu',person.last_name)

    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person = Person("123", "Vu")
        with self.assertRaises(ValueError):
            person = Person("Vic", "123")

    def test_person_str(self):
        person = Person('Vic', 'Vu')
        self.assertEqual('Vic,Vu',str(person))

class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        employee=Employee('Vic','Vu',
                          "1900-01-01",3)
        self.assertEqual('Vic',employee.first_name)
        self.assertEqual('Vu', employee.last_name)
        self.assertEqual('1900-01-01', employee.review_date)
        self.assertEqual(3,employee.review_rating)

    def test_employee_invalid_review_date_format(self):
        with self.assertRaises(ValueError):
            employee = Employee('Vic', 'Vu',
                                "01-01-1900", 3)

    def test_employee_review_rating_out_of_range(self):
        with self.assertRaises(ValueError):
            employee = Employee('Vic', 'Vu',
                                "01-01-1900", 7)

    if __name__=='__main__':
        unittest.main()