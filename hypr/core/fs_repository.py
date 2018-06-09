
import os
import os.path

class FileSystemRepo:
  def __init__(self, base_dir, resource_type):
    self.base_dir = base_dir
    self.resource_type = resource_type


  def path_for(self, key):
    return os.path.join(self.base_dir, key, f'{self.resource_type}.txt')


  def set(self, key, value):
    if self.get(key) == None:
      self.write(key, value)

    return value


  def get(self, key):
    path = self.path_for(key)

    if not os.path.exists(path):
      return None

    with open(path) as file:
      value = file.read()

    return value


  def get_all(self):
    values = []

    if not os.path.exists(self.base_dir):
      return values

    for key in os.listdir(self.base_dir):
      with open(self.path_for(key)) as file:
        values.append(file.read())

    return values


  def write(self, key, value):
    target_dir = os.path.join(self.base_dir, key)
    os.makedirs(target_dir)
    target_file = self.path_for(key)

    with open(target_file, 'w+') as file:
      file.write(value)
