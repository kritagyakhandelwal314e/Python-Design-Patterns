class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls)\
                            .__call__(*args, **kwargs)
    return cls._instances[cls]

class Database(metaclass=Singleton):

  def __init__(self):
    print('loading a database from file')


if __name__ == '__main__':
  d1 = Database() # init will be called
  d2 = Database() # init won't be called
  print(d1 is d2)
