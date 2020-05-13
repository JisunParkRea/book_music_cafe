import os, sys, json
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
from django.core.exceptions import ImproperlyConfigured

from .models import Music


# Get CLIENT_ID, CLIENT_SECRET from secrets.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, 'secrets.json') # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets['spotify'][setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

client_id = get_secret("CLIENT_ID")
client_secret = get_secret("CLIENT_SECRET")

lz_uri = 'spotify:playlist:37i9dQZEVXbMDoHDwVN2tF?si=w-CyWFTgSy-citDFPA8hpw' # Global top 50
#lz_uri = 'spotify:playlist:37i9dQZEVXbLRQDuF5jeBp?si=mUMcqtGMREySk1SLIUfY5Q' # United States top 50

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.playlist_tracks(lz_uri)

name = []
artists = []
cover_img = []
for track in results['tracks']['items'][:20]:
    name.append(track['track']['name'])
    artists.append([ i['name'] for i in track['track']['artists'] ])
    cover_img.append(track['track']['album']['images'][1]['url'])

try:
    music = Music.objects.get(title=name[0])
except:
    left = Music.objects.all()
    left.delete()
    music = Music(title=name[0], artist=artists[0][0], cover_img=cover_img[0])
    music.save()


# for track in results['tracks']['items'][:20]:
#     print('track    : ' + track['track']['name'])
#     print('artists   : ', end='')
#     for i in track['track']['artists']:
#         print(i['name'], end=', ')
#     print('\ncover art: ' + track['track']['album']['images'][1]['url'])
#     print('\n')
