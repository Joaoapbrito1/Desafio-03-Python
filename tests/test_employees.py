import pytest
from models.employees import RegularEmployee, Manager
from models.hr_system import HRSystem

def test_regular_employee_bonus():
    e = RegularEmployee("John", 1000)
    assert e.calculate_bonus() == 100

def test_manager_bonus():
    m = Manager("Mary", 2000, 500)
    assert m.calculate_bonus() == 2000 * 0.2 + 500

def test_set_salary_negative():
    e = RegularEmployee("John", 1000)
    with pytest.raises(ValueError):
        e.set_salary(-100)

def test_show_bonus_prints(capsys):
    e = RegularEmployee("John", 1000)
    hr = HRSystem()
    hr.show_bonus(e)
    captured = capsys.readouterr()
    assert "John - Bonus: 100.0" in captured.out
    assert "[LOG] Bonus action registered." in captured.out

def test_list_bonuses(capsys):
    hr = HRSystem()
    e1 = RegularEmployee("John", 1000)
    e2 = Manager("Mary", 2000, 500)
    hr.register_employee(e1)
    hr.register_employee(e2)
    hr.list_bonuses()
    captured = capsys.readouterr()
    assert "John - Bonus: 100.0" in captured.out
    assert "Mary - Bonus: 900.0" in captured.out