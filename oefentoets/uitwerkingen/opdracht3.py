import math

class Employee:
    departmentEmployedCount = {}

    def __init__(self, name, role, department, salary, isTemporary = False):
        self.name = name;
        self.role = role;
        self.department = department;
        self.salary = salary;
        self.isTemporary = isTemporary
        if self.departmentEmployedCount.get(department) == None:
            self.departmentEmployedCount[department] = {"managers": 0,
                "employees": 0}

        if self.role == "manager":
            self.departmentEmployedCount[department]["managers"] += 1
        else:
            self.departmentEmployedCount[department]["employees"] += 1

    def __repr__(self):
        return self.name+", "+self.role+", "+\
            str(self.getYearlyIncome())+", "+str(self.isTemporary)

    def getYearlyIncome(self):
        yearlyNumeric = self.salary * 12
        yearlyIncome = "€"+str(round(yearlyNumeric / 1000, 3))+"k"
        return yearlyIncome


class Management(Employee):
    def __init__(self, name, role, department, salary, bonus, isTemporary = False):
        super().__init__(name, role, department, salary, isTemporary)
        self.bonus = bonus

    def __repr__(self):
        return super().__repr__()

    def getManagementBonus(self):
        standardBonusPercentage = (self.bonus / 100)
        employeeBonusPercentage = self.getEmployeeBonus(self.department)
        return standardBonusPercentage + employeeBonusPercentage + 1

    def getEmployeeBonus(self, department):
        employeesCount = super().departmentEmployedCount[department]["employees"]
        managersCount = super().departmentEmployedCount[department]["managers"]
        employeesBonusTotal = employeesCount * .005
        return employeesBonusTotal / managersCount

    def getYearlyIncome(self):
        yearlyNumeric = (self.salary * 12) * self.getManagementBonus()
        yearlyIncome = "€"+str(round(yearlyNumeric / 1000, 3))+"k"
        return yearlyIncome


company = []
company.append(Employee('Johnson', 'sr. clerc', 'finance', 2300, False))
company.append(Management('Bush jr.', 'manager', 'finance', 5400, 10, True))
company.append(Employee('Jasons', 'clerc', 'finance', 1900, False))
company.append(Management('Bushes', 'manager', 'R&D', 5400, 10, True))
company.append(Employee('Hunter', 'researcher', 'R&D', 2300, False))
company.append(Employee('Vries', 'researcher', 'R&D', 2300, False))
company.append(Employee('Locker', 'researcher', 'R&D', 2300, False))
company.append(Management('Schneier', 'manager', 'R&D', 6400, 10, True))

for employee in company:
    print(employee)

print(Employee.departmentEmployedCount)
