from django.conf import settings
from hypr.core.fs_repository import FileSystemRepo

class ProfilePicturesRepo(FileSystemRepo):
  def __init__(self):
    super().__init__(base_dir=settings.USER_DATA_DIR, resource_type='profile_picture')
