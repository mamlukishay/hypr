import os.path

TWITTER_BASE_URL = 'https://twitter.com'

def profile_pic_url_for_handler(handler):
  return os.path.join(TWITTER_BASE_URL, handler, 'photo')
