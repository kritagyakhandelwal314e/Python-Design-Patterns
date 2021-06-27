class CEO:
  __shared_state = {
    'name': 'Steve',
    'age': 55
  }
  def __init__(self):
    self.__dict__ = self.__shared_state

  def __str__(self):
    return f'{self.name} is {self.age} years old'

class Monostate:
  _shared_state = {}
  def __new__(cls, *args, **kwargs):
    obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_state
    return obj

class CFO(Monostate):
  def __init__(self):
    self.name = ''
    self.money_managed = 0

  def __str__(self):
    return f'{self.name} managed ${self.money_managed}'

if __name__ == '__main__':
  ceo1 = CEO()
  print(ceo1)
  ceo2 = CEO()
  ceo2.age = 77
  print(ceo1)
  print(ceo2)
  print(ceo1 is ceo2) # False
  print(id(ceo1))
  print(id(ceo2))

  cfo1 = CFO()
  cfo1.name = 'Kritagya'
  cfo1.money_managed = 1000000000
  print(cfo1)

  cfo2 = CFO()
  cfo2.name = 'Yash'
  cfo2.money_managed = 9999999999
  print(cfo2)
  print(cfo1)
  print(id(cfo1))
  print(id(cfo2))
  print(cfo1 is cfo2)