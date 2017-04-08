                #INSTABOTS#

#import libraries
import requests

Access_Token="2338013941.3fe8729.65d7a6c1f3f84fdbb2e2ac56150b5934"      #self generated token from instagram/develeper
base_url="https://api.instagram.com/v1"             #common url


# information of owner #
def self_info():
    request_url=base_url+"/users/self/?access_token="+Access_Token
    my_info= requests.get(request_url).json()

    print my_info['data']['full_name']
    #print my_info['data']['id']
    print my_info['data']['profile_picture']

self_info()
#https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN


#information of other users
def insta_users_search(user_name):
    url_user = base_url + "/users/search?q==" + user_name + "&access_token=" + Access_Token
    user_info = requests.get(url_user).json()
    #print user_info
    print user_info['data'][0]['full_name']
    #print user_info['data'][0]['id']
    return user_info['data'][0]['id']
    #print user_info['data'][0]['profile_picture']
#insta_users_search(user_name="gobind.gobind")



# recent post of users
def recent_post(insta_username):
    user_id=insta_users_search(insta_username)
    url_user = base_url + "/users/" + user_id + "/media/recent/?access_token=" + Access_Token   #https://api.instagram.com/v1/users/self/media/recent/?access_token=ACCESS-TOKEN
    #print url_user
    recent_posts=requests.get(url_user).json()
    print recent_posts['data'][1]['link']
    return recent_posts['data'][1]['id']

#recent_post(insta_username="just_rawat")



def like_post(insta_username):
    post_id=recent_post(insta_username)
    print post_id
    payload={"access_token":Access_Token}
    request_url=base_url+ "/media/" + post_id + "/likes"
    response_to_like=requests.post(request_url,payload).json()
    if response_to_like['meta']['code'] == 200:
        print("The post has been liked.")
        print response_to_like
    else:
        print("Some error occurred! Try Again.")

like_post("gobind.gobind")


def post_comment(insta_username):
    media_id=recent_post(insta_username)
    payload=(base_url+"/media/%s/comments?access_token=%s") %(media_id,Access_Token)
    request_data={"access_token":Access_Token,'text':'hulle hullareee hule hule'}
    comment_request=requests.post(payload,request_data).json()
    if comment_request['meta']['code'] == 200:
        print("The post has been liked.")
        print comment_request
    else:
        print("Some error occurred! Try Again.")




#post_comment(insta_username="gobind.gobind")

#https://api.instagram.com/v1/media/{media-id}/comments?access_token=ACCESS-TOKEN
def get_comments(insta_username):
    media_id=recent_post(insta_username)
    request_data=base_url+ "/media/" + media_id +"/comments?access_token="+Access_Token
    comment=requests.get(request_data).json()

    return comment['data'][0]['id']
   # print comment['data'][1]['text']
#get_comments(insta_username="gobind.gobind")


#https://api.instagram.com/v1/media/{media-id}/comments/{comment-id}?access_token=Access_Token
def comment_del(insta_username):
    media_id = recent_post(insta_username)
    comment_id=get_comments(insta_username)
    #print comment_id
    request_url=base_url+ "/media/" + media_id + "/comments/" + comment_id+ "?access_token=" + Access_Token
    comments=requests.delete(request_url).json()
    if comments['meta']['code'] == 200:
        print("The post has been liked.")
        print comments
    else:
        print("Some error occurred! Try Again.")
        print comments



comment_del(insta_username="gobind.gobind")


