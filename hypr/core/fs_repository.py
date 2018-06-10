
import os
import os.path
from django.conf import settings

BASE_DIR = settings.DATA_DIR
class FileSystemRepoMixin:
  def __init__(self, resource_type = None):
    self.resource_type = resource_type


  def path_for(self, key):
    return os.path.join(BASE_DIR, key, f'{self.resource_type}.txt')


  def set(self, key, value):
    target_dir = os.path.join(BASE_DIR, key)
    
    if not os.path.exists(target_dir):
      os.makedirs(target_dir)
    
    target_file = self.path_for(key)
    with open(target_file, 'w+') as file:
      file.write(value)

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

    if not os.path.exists(BASE_DIR):
      return values

    for key in os.listdir(BASE_DIR):
      with open(self.path_for(key)) as file:
        values.append(file.read())

    return values


  def keys(self):
    if not os.path.exists(BASE_DIR):
      return []

    return os.listdir(BASE_DIR)

