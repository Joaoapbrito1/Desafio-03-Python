# Startup Employee System

This project is a system for calculating employee bonuses in a startup, developed with a focus on Object-Oriented Programming (OOP) and automated testing.

## Description

The startup has two types of employees: **regular employees** and **managers**. The Human Resources (HR) department wants to log all actions related to bonuses and ensure the correctness of the calculations. The system is designed to be modular, testable, and extensible.

## Objective

- Implement classes and methods using OOP concepts.
- Write automated tests to ensure the correct functioning of the system.

## Features

### 1. Class Creation

- **Abstract class `Employee`:**
  - Two private attributes: `name` and `salary`.
  - Abstract method: `calculate_bonus`.
  - Public methods:
    - `get_name`: returns the name.
    - `get_salary`: returns the salary.
    - `set_salary`: updates the salary (does not allow negative values).
- **Class `RegularEmployee` (inherits from `Employee`):**
  - Implements `calculate_bonus`, returning 10% of the salary.
- **Class `Manager` (inherits from `Employee`):**
  - Extra attribute: `additional_bonus`.
  - Implements `calculate_bonus`, returning 20% of the salary plus `additional_bonus`.

### 2. Logging Decorator

- `log_action`: decorator that displays a log message whenever a bonus is shown on the screen.

### 3. System Class

- `HRSystem`:
  - Method `show_bonus`, decorated with `@log_action`, which receives an employee and displays their name and bonus.

### 4. Usage
1. Clone the repository:

 ```bash
 git clone [https://github.com/Joaoapbrito1/Desafio-03-Python.git](https://github.com/Joaoapbrito1/Desafio-03-Python.git)

```
2. Install dependencies (for testing):
```bash
pip install pytest
```
3. Run the main example:
```bash
python main.py
```
4. Run the tests:
```bash
pytest test_employees.py
```

## File Structure

- `employees.py`: Classes `Employee`, `RegularEmployee`, and `Manager`.
- `hr_system.py`: Class `HRSystem` and the `log_action` decorator.
- `test_<testname>.py`: Automated tests using `pytest`.

## Extra Challenge (Optional)

- Implement an internal list in the `HRSystem` class to store all registered employees.
- Create the `list_bonuses` method, which displays the bonus of all employees using polymorphism.

---
## License

MIT License

Feel free to contribute or suggest improvements!