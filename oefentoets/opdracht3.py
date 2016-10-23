class Employee:

    employees = {}


    def __init__(self, name, role, departement, salary, isTemporary=True):
        self.name = name
        self.isTemporary = isTemporary
        self.role = role
        self.salary = salary
        self.departement = departement
        if (self.employees.get(departement)) == None:
            counter = 0
        else:
            counter = self.employees.get(departement)
        self.employees.update({departement:counter+1})

    def money_in_k(self, money):
        return money/1000

    def yearly_income(self):
        return (self.money_in_k(12*self.salary))

    def __repr__(self):
        return ('Employee: %s, %s, %s, €%sk, %s' % (self.name, self.role, self.departement, self.yearly_income(),
                self.isTemporary))


class Management(Employee):

    managers = {}

    def __init__(self, name, role, departement, salary, bonus, isTemporary):
        Employee.__init__(self, name, role, departement, salary, isTemporary)
        self.bonus = bonus
        if (self.managers.get(departement))==None:
            counter = 0
        else:
            counter = self.managers.get(departement)
        self.managers.update({departement:counter+1})

    def __repr__(self):
        return ('Management: %s, %s, %s, €%sk, %s' % (self.name, self.role, self.departement, self.yearly_income(),
                self.isTemporary))

    def yearly_income(self):
        yearly_salery = 12 * self.salary
        employee_bonus = ((Employee.employees.get(self.departement) - self.managers.get(self.departement)) * 0.5) / \
                         self.managers.get(self.departement)
        yearly_bonus =  yearly_salery * (1.0+(self.bonus + employee_bonus)/100)
        return self.money_in_k(yearly_bonus)




company = []
company.append(Employee('Johnson', 'sr. clerc', 'finance', 2300, False))
company.append(Management('Bush jr.', 'manager', 'finance', 5400, 10, True))
company.append(Employee('Jasons', 'clerc', 'finance', 1900, False))
company.append(Management('Bushes', 'manager', 'R&D', 5400, 10, True))
company.append(Employee('Hunter', 'researcher', 'R&D', 2300, False))
company.append(Employee('Vries', 'researcher', 'R&D', 2300, False))
company.append(Employee('Locker', 'researcher', 'R&D', 2300, False))
company.append(Management('Schneier', 'manager', 'R&D', 6400, 10, True))
print(Management.managers, Employee.employees)


for employee in company:
    print(employee)
