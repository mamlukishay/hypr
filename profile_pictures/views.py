import json
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from profile_pictures.repositories import ProfilePicturesRepo
from profile_pictures.interactions import store_profile_pic_for_twitter_handle

def index(request):
  if request.method == 'GET':
    return list_handles()  
  elif request.method == 'POST':
    return create_profile_picture(request)
  else:
    return HttpResponseNotFound

def create_profile_picture(request):
  payload = json.loads(request.body)
  
  if payload:
    profile_pic = store_profile_pic_for_twitter_handle.run(payload['handle'])
    return JsonResponse({'profile_picture': profile_pic})
  else:
    return HttpResponseBadRequest('Missing user handle')

def list_handles():
  handles = ProfilePicturesRepo().keys()
  return JsonResponse({'handles': handles})
