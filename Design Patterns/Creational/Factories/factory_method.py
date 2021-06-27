from enum import Enum
from math import *

class CoordinateSystem(Enum):
  CARTESIAN = 1
  POLAR = 2

class Point:
  # commonly we do like this
  # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
  #   if system == CoordinateSystem.CARTESIAN:
  #     self.x = a
  #     self.y = b
  #   elif system == CoordinateSystem.POLAR:
  #     self.x = a * cos(b)
  #     self.y = a * sin(b)

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f'x: {self.x}, y: {self.y}'


  # Below are the Factory Methods
  @staticmethod
  def new_cartesion_point(x, y):
    return Point(x, y)

  @staticmethod
  def new_polar_points(rho, theta):
    return Point(rho * cos(theta), rho * sin(theta))

if __name__ == '__main__':
  p = Point(2, 3)
  p2 = Point.new_polar_points(2, 3)
  print(p)
  print(p2)