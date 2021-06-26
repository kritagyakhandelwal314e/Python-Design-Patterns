# Open Close Principle
"""
open for extension (inherit and do modification)
closed for modification
"""

from enum import Enum

class Color(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3

class Size(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3

class Weight(Enum):
  LITE = 1
  NORMAL = 2
  HEAVY = 3

class Product:
  def __init__(self, name, color, size, weight):
    self.name = name
    self.color = color
    self.size = size
    self.weight = weight

# This approach does not scale is added more criterias 
# for example we add weight also
class ProductFilter:
  def filter_by_color(self, products, color):
    for product in products:
      if product.color == color:
        yield product

  def filter_by_size(self, products, size):
    for product in products:
      if product.size == size:
        yield product
  
  def filter_by_size_and_color(self, products, size, color):
    for product in products:
      if product.size == size and product.color == color:
        yield product

# Specification
class Specification:
  def is_satisfied(self, item):
    pass

  def __and__(self, other):
    return AndSpecification(self, other)

class Filter:
  def filter(self, items, spec):
    pass

class ColorSpeccification(Specification):
  def __init__(self, color):
    self.color = color

  def is_satisfied(self, item):
    return item.color == self.color

class SizeSpeccification(Specification):
  def __init__(self, size):
    self.size = size

  def is_satisfied(self, item):
      return item.size == self.size

class WeightSpecification(Specification):
  def __init__(self, weight):
    self.weight = weight

  def is_satisfied(self, item):
    return self.weight == item.weight

class AndSpecification(Specification):
  def __init__(self, *args):
    self.args = args
  
  def is_satisfied(self, item):
    return all(map(lambda spec: spec.is_satisfied(item), self.args))

class BetterFilter(Filter):
  def filter(self, items, spec):
    for item in items:
      if spec.is_satisfied(item):
        yield item

if __name__ == '__main__':
  apple = Product('Apple', Color.GREEN, Size.SMALL, Weight.LITE)
  tree = Product('Tree', Color.GREEN, Size.LARGE, Weight.NORMAL)
  house = Product('House', Color.BLUE, Size.LARGE, Weight.HEAVY)

  products = [apple, tree, house]
  pf = ProductFilter()
  print('Green Products (old):')
  for product in pf.filter_by_color(products=products, color=Color.GREEN):
    print(f' - {product.name} is green')
  
  bf = BetterFilter()
  print('Green Products (new):')
  green = ColorSpeccification(Color.GREEN)
  for product in bf.filter(items=products, spec=green):
    print(f' - {product.name} is green')

  print('Large Products (new):')
  large = SizeSpeccification(Size.LARGE)
  for product in bf.filter(items=products, spec=large):
    print(f' - {product.name} is large')

  print('Large and Blue Products (new):')
  large_blue = large & ColorSpeccification(Color.BLUE)
  for product in bf.filter(items=products, spec=large_blue):
    print(f' - {product.name} is large and blue')
  
  print('Large and Blue and Heavy Products (new):')
  large_blue_heavy = large & ColorSpeccification(Color.BLUE) & WeightSpecification(Weight.HEAVY)
  for product in bf.filter(items=products, spec=large_blue_heavy):
    print(f' - {product.name} is large and blue and heavy')