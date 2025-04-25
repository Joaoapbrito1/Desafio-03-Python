from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = new_salary

class RegularEmployee(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.10

class Manager(Employee):
    def __init__(self, name, salary, extra_bonus):
        super().__init__(name, salary)
        self.extra_bonus = extra_bonus

    def calculate_bonus(self):
        return self.get_salary() * 0.20 + self.extra_bonus