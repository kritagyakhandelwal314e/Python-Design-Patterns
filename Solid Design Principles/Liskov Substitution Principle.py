# Liskov Substitution Principle (LSP)

class Rectangle:
  def __init__(self, width, height) -> None:
    self._width = width
    self._height = height

  @property
  def area(self):
    return self.width * self.height

  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, value):
    self._width = value

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, value):
    self._height = value

  def __str__(self):
    return f'Width: {self.width}, height: {self.height}'

def use_it(rc):
  w = rc.width
  rc.height = 10
  expected = w*10
  print(f'Expected an area of {expected}, and got {rc.area}')

# this class violates the LSP for function use_it
class Square(Rectangle):
  def __init__(self, size):
    Rectangle.__init__(self, size, size)

  @Rectangle.width.setter
  def width(self, value):
    self._width = self._height = value

  @Rectangle.height.setter
  def height(self, value):
    self._width = self._height = value


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
