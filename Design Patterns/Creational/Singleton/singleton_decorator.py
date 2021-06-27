def singleton(class_):
  instances = {}

  def get_instance(*args, **kwargs):
    if class_ not in instances:
      instances[class_] = class_(*args, **kwargs)
    return instances[class_]

  return get_instance


@singleton
class Database:

  def __init__(self):
    print('loading a database from file')

  # below block won't work because with help of decorator Database became function
  # def __new__(cls, *args, **kwargs):
  #   if not cls._instance:
  #     cls._instance = super(Database, cls)\
  #                     .__new__(cls, *args, **kwargs)
  #   return cls._instance

if __name__ == '__main__':
  d1 = Database() # init will be called
  d2 = Database() # init won't be called
  print(d1 is d2)