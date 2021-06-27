class Database:
  _instance = None

  def __init__(self):
    print('loading a database from file')

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(Database, cls)\
                      .__new__(cls, *args, **kwargs)
    return cls._instance

if __name__ == '__main__':
  d1 = Database() # init will be called
  d2 = Database() # init will still be called
  print(d1 is d2)