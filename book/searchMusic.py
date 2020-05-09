import os, sys, json
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
from django.core.exceptions import ImproperlyConfigured


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

lz_uri = 'spotify:artist:6VuMaDnrHyPL1p4EHjYLi7' # Charlie Puth

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.artist_top_tracks(lz_uri)

# get top 10 tracks
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
