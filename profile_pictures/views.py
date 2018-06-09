from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json
import os.path

def index(request):
  if request.method == 'GET':
    handlers = get_all_handlers()
    return HttpResponse(handlers)
  if request.method == 'POST':
    body = json.loads(request.body)
    profile_pic = get_profile_pic(body['handler'])
    return HttpResponse(profile_pic)

def get_all_handlers():
  retval_handlers = []
  handlers_path = os.path.join(settings.DATA_DIR, settings.HANDLERS_FILENAME)

  if os.path.exists(handlers_path):
    handlers_file = open(handlers_path)
    retval_handlers = handlers_file.readlines()
    handlers_file.close()
  else:
    retval_handlers = 'no'

  return retval_handlers

def get_profile_pic(handler):
  set_handler(handler)
  return generate_profile_pic_link_for(handler)

def generate_profile_pic_link_for(handler):
  twitter_base_url = 'https://twitter.com'
  return os.path.join(twitter_base_url, handler, 'photo')

def set_handler(handler):
  if not handler_exist(handler):
    write_handler(handler)
  
  return handler

def handler_exist(handler):
  return False

def write_handler(handler):
  handlers_path = os.path.join(settings.DATA_DIR, settings.HANDLERS_FILENAME)
  handlers_file = open(handlers_path, 'a+')
  handlers_file.write(f'{handler}\r\n')
  handlers_file.close()

