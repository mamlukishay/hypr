import os.path

TWITTER_BASE_URL = 'https://twitter.com'

def profile_pic_url_for_handle(handle):
  return os.path.join(TWITTER_BASE_URL, handle, 'photo')
