import requests
from .structures import Profile, Rant
import time

api_base = "https://devrant.com/api"
app_id = 3

def isValidUser(username):
    return requests.get(api_base + "/get-user-id", params={"app": app_id, "username": username}).json()["success"]

def fetchProfile(username):
    user_id = requests.get(api_base + "/get-user-id", params={"app": app_id, "username": username}).json()["user_id"]
    
    user_profile = requests.get(api_base + "/users/" + str(user_id), params={"app": app_id}).json()

    return (user_profile, user_id)

def profile2Profile(profile, user_id):
    output = Profile()

    output.username = profile["profile"]["username"]
    output.user_id = user_id
    output.score = profile["profile"]["score"]
    output.profile_pic_gen = "https://avatars.devrant.com/" + profile["profile"]["avatar"]["i"]
    output.profile_pic_uri = ""
    output.bio = profile["profile"]["about"]
    output.skills = profile["profile"]["skills"]
    output.location = profile["profile"]["location"]
    output.website = profile["profile"]["website"]
    output.github = profile["profile"]["github"]
    output.creation_date = profile["profile"]["created_time"]
    output.rant_count = profile["profile"]["content"]["counts"]["rants"]
    output.comment_count = profile["profile"]["content"]["counts"]["comments"]
    output.upvote_count = profile["profile"]["content"]["counts"]["upvoted"]
    output.fav_count = profile["profile"]["content"]["counts"]["favorites"]
    output.rants = profile["profile"]["content"]["content"]["rants"]
    output.comments = profile["profile"]["content"]["content"]["comments"]
    output.upvoted = profile["profile"]["content"]["content"]["upvoted"]
    output.favs = profile["profile"]["content"]["content"]["favorites"]
    
    return output

def getRantPage(uid, i):
    rants = requests.get(api_base + "/users/" + str(uid), params={"app": app_id, "skip": i}).json()["profile"]["content"]["content"]["rants"]

    for rant in rants:
        output = Rant()

        output.author_name = rant["user_username"]
        output.body = rant["text"]
        output.score = rant["score"]
        output.comment_count = 0
        output.comments = []
        output.date = rant["created_time"]

        yield output
            
