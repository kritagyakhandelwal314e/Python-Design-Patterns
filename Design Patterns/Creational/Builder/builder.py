# constructing a HTML builder
text = "Hello There"
parts = ['<p>', text, '</p>']
print(''.join(parts))

words = ['Hello', 'There']
parts = ['<ul>']
for word in words:
  parts.append(f'\t<li>{word}</li>')

parts.append('</ul>')

print('\n'.join(parts))


class HtmlElement:
  indent_size = 2

  def __init__(self, name='', text=''):
    self.text = text
    self.name = name
    self.elements = []

  def __str(self, indent):
    lines = []
    i = ' ' * (indent * self.indent_size)
    lines.append(f'{i}<{self.name}>')
    if self.text:
      i1  = ' ' * ((indent + 1) * self.indent_size)
      lines.append(f'{i1}{self.text}')
    for e in self.elements:
      lines.append(e.__str(indent + 1))
    lines.append(f'{i}</{self.name}>')
    return '\n'.join(lines)

  def __str__(self):
    return self.__str(0)

  @staticmethod
  def create(name):
    return HtmlBuilder(name)

class HtmlBuilder:
  def __init__(self, root_name):
    self.root_name = root_name
    self.__root = HtmlElement(name=root_name)
  
  def add_child(self, child_name, child_text):
    self.__root.elements.append(
      HtmlElement(child_name, child_text)
    )

  def add_child_fluent(self, child_name, child_text): # for chaining
    self.__root.elements.append(
      HtmlElement(child_name, child_text)
    )
    return self

  def __str__(self):
    return str(self.__root)

builder = HtmlElement.create('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'there')
builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'there')
print('ordinary builder:')
print(builder)