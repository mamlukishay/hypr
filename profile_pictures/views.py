import json
from django.shortcuts import render
from django.http import HttpResponse
from profile_pictures import repository as profile_pics_repo
from services.twitter import profile_pic_url_for_handler

def index(request):
  if request.method == 'GET':
    return HttpResponse(profile_pics_repo.get_all())
  if request.method == 'POST':
    payload = json.loads(request.body)
    profile_pic = store_profile_pic_for_handler(payload['handler'])
    return HttpResponse(profile_pic)

def store_profile_pic_for_handler(handler):
  pic_url = profile_pic_url_for_handler(handler)
  profile_pics_repo.set(key=handler, value=pic_url)
  return pic_url