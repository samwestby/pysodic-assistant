# Adoption from github.com/shivasiddharth/GassistPi/master/src/actions.py
# and https://github.com/balloob/pychromecast/blob/f5a92cd816245ba53820a7ac3b63ec18acd5f8f1/examples/spotify_example.py

import spotipy.util as util
import json
import os
import spotipy

# Spotify Declarations
# Register with spotify for a developer account to get client-id and client-secret
# if Spotify_credentials:
with open(r"scripts/oauth/spotify_creds.json") as f:
    spotify_creds = json.load(f)
client_id = spotify_creds['client_id']
client_secret = spotify_creds['client_secret']
username = spotify_creds['username']
scope = 'user-modify-playback-state'
redirect_uri = "https://www.google.com"
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# This code below helps us find available devices through Spotify connect
# scope = "user-read-playback-state"
# device_access_token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
# sp_device = spotipy.Spotify(auth=device_access_token)
# results = sp_device.devices()
# print(results)


def play_spotify(phrase):
    print('playing')
    sp = spotipy.Spotify(auth=token)
    if phrase == 'happy':
        uri = 'spotify:playlist:1JmHekuoq8mkuVmapRSo4c'
    elif phrase == 'sad':
        uri = 'spotify:playlist:3xWxT0SzhFsJeWsLmR5pgJ'
    else:
        return
    sp.start_playback(device_id='OPTIONAL DEVICE ID',
                      context_uri=uri)

def pause_spotify():
    sp = spotipy.Spotify(auth=token)
    sp.pause_playback()


