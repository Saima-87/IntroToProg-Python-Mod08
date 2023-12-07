# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# SaimaAhmed,2023-11-30,Created Script
# ------------------------------------------------------------------------------- #

import json
import tempfile
import unittest

from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name

    def tearDown(self):
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "Bob", "LastName": "Smith", "ReviewDate": "2023-11-30", "ReviewRating": 4},
            {"FirstName": "Sue", "LastName": "Jones", "ReviewDate": "2023-11-30", "ReviewRating": 3}
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_employee_data_from_file method and check if it returns the expected data

        employees = []
        employees = FileProcessor.read_employee_data_from_file(self.temp_file_name, employees, Employee)

        # Assert that the sample_data list contains the expected employee objects
        self.assertEqual(len(sample_data), len(employees))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]["FirstName"], employees[i].first_name)
            self.assertEqual(sample_data[i]["LastName"], employees[i].last_name)
            self.assertEqual(sample_data[i]["ReviewDate"], employees[i].review_date)
            self.assertEqual(sample_data[i]["ReviewRating"], employees[i].review_rating)

    def test_read_employee_data_from_file_FileNotFoundError(self):
        empty_list = []
        try:
            employees= FileProcessor.read_employee_data_from_file('unknown_file.json', empty_list, Employee)
        except FileNotFoundError as e:
            self.assertEqual(str(e)), "Text file must exist before running this script"


    def test_write_employee_data_to_file(self):
        sample_data = [
            Employee('Bob', 'Smith', '2023-11-30', 4),
            Employee('Sue', 'Salias', '2023-11-30', 3)
        ]
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_data)

        with open(self.temp_file_name, 'r') as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(file_data))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i].first_name, file_data[i]["FirstName"])
            self.assertEqual(sample_data[i].last_name, file_data[i]["LastName"])
            self.assertEqual(sample_data[i].review_date, file_data[i]["ReviewDate"])
            self.assertEqual(sample_data[i].review_rating, file_data[i]["ReviewRating"])

    if __name__ == '__main__':
        unittest.main()
