import tweepy
import os
import sys

arg1 = sys.argv[1]
print arg1

# Consumer keys and access tokens, used for OAuth
consumer_key = 'hahaha'
consumer_secret = 'hehehe'
access_token = 'hihihi'
access_token_secret = 'hohoho'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))
 
# Sample method, used to update a status
# api.update_status('Hello Form RBI Lab!')

# load image
imagePath = arg1
status = "Text herererere"

# Send the tweet.
api.update_with_media(imagePath, status)

# Tschuess
sys.exit(0)
