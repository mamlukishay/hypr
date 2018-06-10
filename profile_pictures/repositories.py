from hypr.core.fs_repository import FileSystemRepoMixin

class ProfilePicturesRepo(FileSystemRepoMixin):
  def __init__(self):
    super().__init__(resource_type='profile_picture')
