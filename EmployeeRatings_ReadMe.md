My Github repository can be found [here](https://github.com/Saima-87/IntroToProg-Python-Mod08)

# Creating a Python Script

## Introduction:
So far we have learned how to write code, organize code into functions, then organize functions and data into classes using the SoC design pattern.
In this module we will learn how applications are designed and created, an additional organization option, and ways to test our code before it is released. 

## Applications:
An application is a set of one or more files that perform a set of tasks. In this course we have focused on creating single file programs to perform all the tasks we needed. 
In software development, the terms "program" and "application" can sometimes be used interchangeably, but a program is generally a smaller amount of code with few specific tasks, while an application is a larger and more comprehensive software program designed for end-users with a broader range of features that may include a graphical user interface.

## Code Modules:
Code modules (or just modules) are Python code files used by other code files. Within a code module file, you can create a set of functions and classes, then link the module to another code file to use those functions and classes. 

## Designing Applications:
Designing and creating an application is an iterative process that involves problem analysis, architectural design, and implementing basic development principles. Having a general idea of how applications are made is a valuable experience that prepares you to create real-world projects, so let's look at a simple example using our lab code.
Here is a basic list the steps need to create an application:
-	Problem Analysis 
-	Requirements Gathering 
-	Architectural Design: 
-	Choosing Development Tools 
-	Software Development 
-   Testing and Quality Assurance
-	User-Centered Design
-	Project Documentation
-	Deployment and Scaling
-	Continuous Improvement

## Testing and Quality Assurance:
Rigorous testing and quality assurance processes are essential, including unit testing, integration testing, and user acceptance testing.
One of the easiest ways to deal with this is by performing tests on each individual unit of the code. Which is what we will look at next. 

## Unit Testing:
Unit testing involves subjecting each individual unit of code, such as functions or methods, to a battery of tests to ensure that they function correctly in isolation. 
This proactive approach not only aids in detecting errors early but also contributes to more robust and maintainable software, as issues are addressed promptly, reducing the risk of accumulating complex and hard-to-debug problems over time.
We create unit tests by defining functions that "exercise" the properties and methods of our code. Typically, these testing functions are in a separate module file, often referred to as a "test harness." 

## Python’s unit test Framework:
Python's unit test framework is a set of tools for writing and running unit tests. It is inspired by the testing frameworks used in other programming languages, such as JUnit for Java. 
The primary purpose of the unittest framework is to automate the testing of individual components (units) of Python code to ensure that they behave as expected.

# Creating the Program:
The objective of this week’s assignment is to create a multi module application and later testing it by unit testing. 
We take input from the user for the employees first name, last name, employment review data and review rating. 

-   I started the program by first dividing the application into four modules. _‘Main module’_ is the one where our actual program is. 
-	 _‘Data_classes’_ module has all the classes related to the user. Here I used a class **Person** and its sub class **Employee**. 
-	The module named _Processing_classes_ has a class called **FileProcessor** which has 2 functions: **read_employee_data_from_file** and **write_employee_data_from_file**
-	The 4th module named Presentation_classes has a class IO which has all the required functions related to the input and output of the program.  
-	All the modules are linked with each other using _‘import’_ command.
- 	The program starts by calling the function read_data_from_file to read data form the json file _EmployeeRatings.json_ 
````python
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)
````

-   Next, we give different options to the user and ask for inputs for employee's first name, last name, employee review date and employee rating.
-   Later, I saved the given data into the json file.
-   The code is shown below:

```` python
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)  # Note this is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Note this is the class name (ignore the warning)
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
````

-   Next step was to test each module for the errors
-   First, I tested Data_classes module. Important to note that we have to import unittest command before testing our script.
- 	The script begins by importing the Person and Employee classes from the data_classes module. The TestPerson function tests the behavior of the Person class by creating an instance of the Person class with the first name ‘Vic’ and last name ‘Vu’ and then prints the resulting person object. The expected output is ‘Vic Vu’

````python
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
````
-   Next I tested the processing_class. I used the functions setup and tear down to create a temporary file and then close it. We created a temporary file because we didn’t want to mess up with the json file which is used in the program for storing our data. For testing purposes only, we created a temporary file and stored list of dictionary in it called sample_data. 
````python
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
````
-   Next i tested my presentation_classes module as shown below. Here i tested 3 functions...test_input_menu_choice, test_input_employee_data, test_input_employee_data_invalid_review_date_format.
Here i used the _patch_ function that is imported from unit test library. 

````python
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
````
# Summary:
In this assignment we were introduced to making multiple modules of our program. 
Also we were introduced to test different blocks of our code by unit testing.
With the knowledge of above two techniques, we surely have simplified our progarm by also adding efficient way of error handling. 
