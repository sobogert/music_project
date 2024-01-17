import logging

from flask import Flask, render_template, redirect, make_response, session
import json

from functions import createStateKey

app = Flask("music project")
app.config.from_file("config.json", load=json.load)
app.secret_key = createStateKey(16);


'''
<!--            <a href="{{url_for('app.login'}}">login</a>-->
'''
@app.route('/')
def hello():
    # ADD STATE LATER
    return render_template("main.html")

#
# @app.route('login')
# def login():
#     client_id = app.config['CLIENT_ID']
#     redirect_uri = app.config['REDIRECT_URI']
#     scope = app.config['SCOPE']
#
#     # state key exists to protext against cross-site forgery attacks
#     state_key = createStateKey(15)
#     session['state_key'] = state_key
#
#     # redirect user to Spotify authorization page
#     authorize_url = 'https://accounts.spotify.com/en/authorize?'
#     parameters = 'response_type=code&client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&scope=' + scope + '&state=' + state_key
#     response = make_response(redirect(authorize_url + parameters))
#
#     return response


# @app.route('/callback')
# def calling():
#     # make sure the response came from Spotify
#     if request.args.get('state') != session['state_key']:
#         return render_template('index.html', error='State failed.')
#     if request.args.get('error'):
#         return render_template('index.html', error='Spotify error.')
#     else:
#         code = request.args.get('code')
#         session.pop('state_key', None)
#
#         # get access token to make requests on behalf of the user
#         payload = getToken(code)
#         if payload != None:
#             session['token'] = payload[0]
#             session['refresh_token'] = payload[1]
#             session['token_expiration'] = time.time() + payload[2]
#         else:
#             return render_template('index.html', error='Failed to access token.')
#
#     current_user = getUserInformation(session)
#     session['user_id'] = current_user['id']
#     logging.info('new user:' + session['user_id'])
#
#     return redirect(session['previous_url'])
