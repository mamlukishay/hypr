import os.path
from django.conf import settings

KEYVAL_DELIMITER = ':'
PROFILE_PICS_PATH = os.path.join(settings.DATA_DIR, settings.PROFILE_PICS_FILENAME)

def set(key, value):
  if get(key) == None:
    write(key, value)

  return value

def get(key):
  if not os.path.exists(PROFILE_PICS_PATH):
    return None

  with open(PROFILE_PICS_PATH) as file:
    current_val = True
    while current_val:
      current_key, current_val = read_keyval_pair(file)
      print(f'CURRKEY: {current_key} <> {key} KEYTOGET')
      if current_key == key:
        print('YESH!', current_val)
        return current_val

  print('NO HAY!')
  return None

def get_all():
  values = []

  if not os.path.exists(PROFILE_PICS_PATH):
    return values

  with open(PROFILE_PICS_PATH) as file:
    current_val = True
    while current_val:
      current_key, current_val = read_keyval_pair(file)
      values.append (current_val)

  return values

def write(key, value):
  with open(PROFILE_PICS_PATH, 'a+') as file:
    file.writelines([
      f'{key}\r\n',
      f'{value}\r\n'
    ])

def read_keyval_pair(file):
  key = file.readline().strip()
  value = file.readline().strip()
  return (key, value)