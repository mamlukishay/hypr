from profile_pictures.repositories import ProfilePicturesRepo
from services import twitter

def run(handle):
  profile_pics_repo = ProfilePicturesRepo()
  pic_url = profile_pics_repo.get(handle)
  
  if not pic_url:
    pic_url = twitter.profile_pic_url_for_handle(handle)
    profile_pics_repo.set(key=handle, value=pic_url)
  
  return pic_url