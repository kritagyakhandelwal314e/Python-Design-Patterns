# Interface Segrigation Principle


class Machine:
  def print(self, document):
    raise NotImplementedError
  
  def fax(self, document):
    raise NotImplementedError
  
  def scam(self, document):
    raise NotImplementedError

class MultiFunctionPrinter(Machine):
  def print(self, document):
    pass

  def fax(self, document):
    pass

  def scan(self, document):
    pass

class OldFashionedPrinter(Machine):
  def print(self, document):
    # ok
    pass

  def fax(self, document):
    pass # no-op

  def scan(self, document):
    pass

# rather do it like this
# grannuler interfaces
class Printer:
  def print(self, document):
    pass

class Scanner:
  def scan(self, document):
    pass

class PhotoCoppier(Printer, Scanner):
  def print(self, document):
    pass
  def scan(self, document):
    pass

class MultiFunctionalMachine(Printer, Scanner):
  def __init__(self, printer, scanner):
    self.scanner = scanner
    self.printer = printer

  def print(self, document):
    self.printer.print(document)

  def scan(self, document):
    self.scanner.scan(document)

