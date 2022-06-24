
from models.userModel import UserModel
###from werkzeug.security import safe_str_cmp

##users = [ User(1,'femi', 'femad')]

##username_mapping = {u.username: u for u in users}
##userid_mapping = {u.id: u for u in users}



def authenticate(username,password):
    ##user = username_mapping.get(username)
    user = UserModel.find_by_username(username)
    
    if user and user.password== password:
        return user

def identity(payload):
    userid = payload['identity']  #### Thus is in webtoken sent by the postman
    return UserModel.find_by_id(userid)    ##userid_mapping.get(userid,None)


    ###eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDkzNzA2NDUsImlhdCI6MTY0OTM3MDM0NSwibmJmIjoxNjQ5MzcwMzQ1LCJpZGVudGl0eSI6MX0.pxIyRPqMd-rK-bbnQLUdoYD0QaLch-uOCuB45XRNkKE
