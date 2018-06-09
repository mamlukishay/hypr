import json
from django.http import JsonResponse
from profile_pictures import repository as profile_pics_repo
from services.twitter import profile_pic_url_for_handler

def index(request):
  if request.method == 'GET':
    handles = profile_pics_repo.get_all()
    return JsonResponse({'handles': handles})
  if request.method == 'POST':
    payload = json.loads(request.body)
    profile_pic = store_profile_pic_for_handle(payload['handle'])
    return JsonResponse({'profile_picture': profile_pic})

def store_profile_pic_for_handle(handle):
  pic_url = profile_pic_url_for_handler(handle)
  profile_pics_repo.set(key=handle, value=pic_url)
  return pic_url