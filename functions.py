import random as rand
import string as string
#from main import app
import logging
import requests
"""
Credit to https://github.com/lucaoh21/Spotify-Discover-2.0/blob/master/functions.py

Creates a state key for the authorization request. State keys are used to make sure that
a response comes from the same place where the initial request was sent. This prevents attacks,
such as forgery.
Returns: A state key (str) with a parameter specified size.
"""


def createStateKey(size):
    # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    return ''.join(rand.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))


"""
Credit to https://github.com/lucaoh21/Spotify-Discover-2.0/blob/master/functions.py

Requests an access token from the Spotify API. Only called if no refresh token for the
current user exists.
Returns: either [access token, refresh token, expiration time] or None if request failed
"""

#
# def getToken(code):
#     token_url = 'https://accounts.spotify.com/api/token'
#     authorization = app.config['AUTHORIZATION']
#     redirect_uri = app.config['REDIRECT_URI']
#
#     headers = {'Authorization': authorization, 'Accept': 'application/json',
#                'Content-Type': 'application/x-www-form-urlencoded'}
#     body = {'code': code, 'redirect_uri': redirect_uri, 'grant_type': 'authorization_code'}
#     post_response = requests.post(token_url, headers=headers, data=body)
#
#     # 200 code indicates access token was properly granted
#     if post_response.status_code == 200:
#         json = post_response.json()
#         return json['access_token'], json['refresh_token'], json['expires_in']
#     else:
#         logging.error('getToken:' + str(post_response.status_code))
#         return None
