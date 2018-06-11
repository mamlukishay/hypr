from profile_pictures.repositories import ProfilePicturesRepo
from social_providers import twitter

def run(handle):
  if not handle:
    return None

  profile_pics_repo = ProfilePicturesRepo()
  pic_url = profile_pics_repo.get(handle)
  
  if not pic_url:
    twitter_user = twitter.TwitterUser(handle)
    pic_url = twitter_user.profile_picture
    profile_pics_repo.set(key=handle, value=pic_url)
  
  return pic_url