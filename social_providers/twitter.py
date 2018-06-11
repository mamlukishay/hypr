import os.path

TWITTER_BASE_URL = 'https://twitter.com'

class User(object):
  def __init__(self, handle):
    self.handle = handle

  def profile_picture(self):
    return os.path.join(TWITTER_BASE_URL, self.handle, 'photo')