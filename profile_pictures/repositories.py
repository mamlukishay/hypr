from hypr.core.fs_repository import FileSystemRepo

class ProfilePicturesRepo(FileSystemRepo):
  def __init__(self):
    super().__init__(resource_type='profile_picture')
