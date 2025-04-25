from models.employees import RegularEmployee, Manager
from models.hr_system import HRSystem

def main():
    hr = HRSystem()

    emp1 = RegularEmployee("João", 3000)
    emp2 = Manager("Maria", 5000, 1200)

    print("=== Bônus individuais ===")
    hr.show_bonus(emp1)
    hr.show_bonus(emp2)

if __name__ == "__main__":
    main()