import os.path

TWITTER_BASE_URL = 'https://twitter.com'

class TwitterUser(object):
  def __init__(self, handle):
    self.handle = handle

  @property
  def profile_picture(self):
    return os.path.join(TWITTER_BASE_URL, self.handle, 'photo')