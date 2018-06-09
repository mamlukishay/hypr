import json
from django.http import JsonResponse
from profile_pictures.repositories import ProfilePicturesRepo
from services import twitter

def index(request):
  if request.method == 'GET':
    handles = ProfilePicturesRepo().keys()
    return JsonResponse({'handles': handles})
  if request.method == 'POST':
    payload = json.loads(request.body)
    profile_pic = store_profile_pic_for_handle(payload['handle'])
    return JsonResponse({'profile_picture': profile_pic})

def store_profile_pic_for_handle(handle):
  profile_pics_repo = ProfilePicturesRepo()
  pic_url = profile_pics_repo.get(handle)
  
  if not pic_url:
    pic_url = twitter.profile_pic_url_for_handle(handle)
    profile_pics_repo.set(key=handle, value=pic_url)
  
  return pic_url