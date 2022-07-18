class Employee:
    def __init__(self, id, firstname, lastname, hourlypay):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.hourlypay = hourlypay

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def getID(self):
        return self.id
    
    def getHourlyPay(self):
        return self.hourlypay

    def setFirstName(self, firstname):
        self.firstname = firstname

    def setLastName(self, lastname):
        self.lastname = lastname

    def setID(self, id):
        self.id = id

    def setHourlyPay(self, hourlypay):
        self.hourlypay = hourlypay

    def pay(self, hoursWorked):
        if float(hoursWorked) <= 40:
            total_pay = int(hoursWorked) * int(self.hourlypay)
            print('-----------------')
            print(f'Name: {self.firstname} {self.lastname}')
            print(f'Employees ID: {self.id}')
            print('-----------------')
            print(f'Check Balance: ${total_pay}')
            print('-----------------')

        elif float(hoursWorked) > 40:
            overtime_pay = float(((int(hoursWorked) - 40) * (int(self.hourlypay) * 1.5)) + (40 * int(self.hourlypay)))
            print('-----------------')
            print(f'Name: {self.firstname} {self.lastname}')
            print(f'Employees ID: {self.id}')
            print('-----------------')
            print(f"Check Balance (Overtime included): ${overtime_pay:.2f}")
            print('-----------------')

new_employee = Employee(input('Please enter employees ID: '),
    input('Please enter employees first name: '),
    input('Please enter employees last name: '),
    float(input('Please enter employees hourly pay: ')))

new_employee.pay(input(f"Enter {new_employee.firstname}'s hours worked: "))