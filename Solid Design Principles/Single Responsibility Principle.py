# Single Responsibility Principle
"""
Dessociating the Responsibily 
into different different classes
"""

class Journal:
  def __init__(self):
    self.entries = []
    self.count = 0
  
  def add_entry(self, text):
    self.count += 1
    self.entries.append(f'{self.count}: {text}')

  def remove_entry(self, pos):
    del self.entries[pos]

  # persistence responsibilty is quite generic 
  # so we should create anouther class for that 
  # so that code can be reused from different classes also
  # def save(self, filename):
  #   file = open(filename, 'w')
  #   file.write(str(self))
  #   file.close()
  
  # def load(self, filename):
  #   pass

  # def load_from_web(self, uri):
  #   pass

  def __str__(self):
    return '\n'.join(self.entries)

class PersistenceManager:
  @staticmethod
  def save_to_file(object_to_save, filename):
    file = open(filename, 'w')
    file.write(str(object_to_save))
    file.close()

  def load(self, filename):
    pass

  def load_from_web(self, uri):
    pass


j = Journal()
j.add_entry('I woke up at 9')
j.add_entry('Learning Design Patterns in Python Very sincerely')
print(f"Journal entries:\n{j}")

file_name = 'journal_file'
PersistenceManager.save_to_file(j, file_name)
print('Verifying file persistence: ')
with open(file_name) as file:
  print(file.read())
