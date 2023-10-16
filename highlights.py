import requests
import json
import os
from datetime import date, timedelta


game_id = '21779'
client_id = 'fvzz1lt9rdkbqip1z1ji30x4acqwgl'
secret = os.environ['TWITCH_API_SECRET']

url = "https://id.twitch.tv/oauth2/token"
headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
data = 'client_id='+client_id+'&client_secret='+secret+'&grant_type=client_credentials'


r = requests.post(url, data=data, headers=headers)

access_token = r.json()['access_token']

today = date.today()
yesterday = date.today() - timedelta(days = 1)

game_url = 'https://api.twitch.tv/helix/clips?game_id=' + game_id + \
    '&started_at=' + str(yesterday) + 'T00:00:00Z&ended_at=' + str(today) + 'T00:00:00Z' 
game_headers = {'Authorization' : 'Bearer ' + access_token, 'Client-Id' : client_id}

raw_clips = requests.get(game_url, headers=game_headers)

print(json.dumps(raw_clips.json(), indent=2))