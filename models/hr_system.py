from models.employees import Employee

def log_action(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Bonus action registered.")
        return func(*args, **kwargs)
    return wrapper

class HRSystem:
    @log_action
    def show_bonus(self, employee: Employee):
        print(f"{employee.get_name()} - Bonus: {employee.calculate_bonus()}")