import os, os.path
from django.conf import settings

BASE_DIR = settings.USER_DATA_DIR
RESOURCE_TYPE = 'profile-picture'

def path_for(key):
  return os.path.join(BASE_DIR, key, f'{RESOURCE_TYPE}.txt')

def set(key, value):
  if get(key) == None:
    write(key, value)

  return value

def get(key):
  path = path_for(key)

  if not os.path.exists(path):
    return None

  with open(path) as file:
    value = file.read()

  return value

def get_all():
  values = []

  if not os.path.exists(BASE_DIR):
    return values

  for key in os.listdir(BASE_DIR):
    with open(path_for(key)) as file:
      values.append(file.read())

  return values

def write(key, value):
  target_dir = os.path.join(BASE_DIR, key)
  os.makedirs(target_dir)
  target_file = path_for(key)

  with open(target_file, 'a+') as file:
    file.write(value)