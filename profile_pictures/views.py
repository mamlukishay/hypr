import json
from django.http import JsonResponse
from profile_pictures.repositories import ProfilePicturesRepo
from profile_pictures.interactions import store_profile_pic_for_twitter_handle

def index(request):
  if request.method == 'GET':
    handles = ProfilePicturesRepo().keys()
    return JsonResponse({'handles': handles})
  
  if request.method == 'POST':
    payload = json.loads(request.body)
    profile_pic = store_profile_pic_for_twitter_handle.run(payload['handle'])
    return JsonResponse({'profile_picture': profile_pic})
