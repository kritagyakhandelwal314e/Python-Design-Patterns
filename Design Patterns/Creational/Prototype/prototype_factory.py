from copy import deepcopy

class Address:
  def __init__(self, street_address, suite, city):
    self.suite = suite
    self.city = city
    self.street_address = street_address

  def __str__(self):
    return f'{self.street_address}, Suite #{self.suite}, {self.city}'

class Employee:
  def __init__(self, name, address):
    self.address = address
    self.name = name

  def __str__(self):
    return f'{self.name} works at {self.address}'

class EmployeeFactory:
  # Prototype Objects
  main_office_employee = Employee(name='', address=Address('123 East Dr', 0, 'London'))
  aux_office_employee = Employee(name='', address=Address('123B East Dr', 0, 'London'))
  
  @staticmethod
  def __new_employee(proto, name, suite):
    result = deepcopy(proto)
    result.name = name
    result.suite = suite
    return result

  @staticmethod
  def new_main_office_employee(name, suite):
    return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)

  @staticmethod
  def new_aux_office_employee(name, suite):
    return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name, suite)


kritagya = EmployeeFactory.new_main_office_employee('Kritagya', '04')
yash = EmployeeFactory.new_aux_office_employee('Yash', '45')

print(kritagya)
print(yash)