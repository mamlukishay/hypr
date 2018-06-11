# hypr

## A few explanations:

* The reuqested enpoints are implemented under the profile_pictures app, which is meant to encapsulate evrything related to the profile pictures resource (routes, models, repo, interactions...) in a single place

* A single endpoint serves both requests: /profile_pictures
  * GET /profile_pictures returns a list of handles that we already scanned and saved to FS
  * POST /profile_pictures scans a profile picture url for a given handle (Only if it weasn't scanned before) and saves it to FS

* Persistency is implemented in the fs_repository class, which need two params in order to function properly - a BASE_DIR and a resource_type. With those in place, data is saved as follows:
  * BASE_DIR contains many dirs, each one of them named as a uniqe key (given on a set op.)
  * Each key dir contains files according to the different resource types.

* The TwitterUser class encapsulates all props and ops related to a twitter user. If needed, this is the place to abstract API calls made to twitter in  order to obtain data. 
  * I didn't do it because the need is not here yet, but possible way to take this in the future is to add an abstract SocialUser class and have TwitterUser and a future FacebookUser(for example) extend it.

* Profile pictures are saved with profile_pictures_repo which mixes the fs_repo in and defines the profile_picture resource type, which creates the following sturcture:
  * BASE_DIR
    * handle1
      * profile_picture.txt (contains profile_pic url for handle1)
    * handle2
      * profile_picture.txt (contains profile_pic url for handle2)

## Assumptions and definitions

* Twitter handles are assumed to be safe to use as dir names (Agreed with Guy)

* Before running the project, please set the DATA_DIR var in settings.py, to define a FS entry point to where the data is going to be saved on your machine.
  * The dir itself doesn't have to exist (will be created on runtime), but the path must be valid 

