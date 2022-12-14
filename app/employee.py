import os

class Employee:
    empCount = 0 # empCount is a class variable

    def __init__(self, first, second, salary):
        # self --> Represents instance of a class
        # self -->
        # first,second,salary are class attributes
        self.first = first
        self.second = second
        self.salary = salary
        Employee.empCount +=1

    @staticmethod
    def display_something(self):
        print("This is a method inside a class")

    def get_salary(self, name):
        return self.salary


    def set_salary(self, salary):
        self.salary = salary

    def double_salary(self):
        return self.salary


def add(a,b):

    return a+b


def multiply(num1, num2):
    return num1*num2