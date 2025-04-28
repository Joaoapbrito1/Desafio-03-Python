from models.employees import Employee

def log_action(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Bonus action registered.")
        return func(*args, **kwargs)
    return wrapper

class HRSystem:
    def __init__(self):
        self.employees = []

    @log_action
    def show_bonus(self, employee: Employee):
        print(f"{employee.get_name()} - Bonus: {employee.calculate_bonus()}")

    def register_employee(self, employee: Employee):
        self.employees.append(employee)

    def list_bonuses(self):
        for emp in self.employees:
            self.show_bonus(emp)