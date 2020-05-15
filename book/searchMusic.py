import os, sys, json
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
from django.core.exceptions import ImproperlyConfigured

from .models import MusicRank1

from .slackBot import slack
from apscheduler.schedulers.background import BackgroundScheduler


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

name = []
artists = []
cover_img = []

def musicChartCheck(): 
    lz_uri = 'spotify:playlist:37i9dQZEVXbMDoHDwVN2tF?si=w-CyWFTgSy-citDFPA8hpw' # Global top 50
    #lz_uri = 'spotify:playlist:37i9dQZEVXbLRQDuF5jeBp?si=mUMcqtGMREySk1SLIUfY5Q' # United States top 50

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.playlist_tracks(lz_uri)

    for track in results['tracks']['items'][:20]:
        name.append(track['track']['name'])
        artists.append([ i['name'] for i in track['track']['artists'] ])
        cover_img.append(track['track']['album']['images'][1]['url'])

    try:
        music = MusicRank1.objects.get(title=name[0])

        # Send a message to #general channel
        slack.chat.post_message('C013UEVAZL0', 'No Change')
    except:
        left = MusicRank1.objects.select_related('title').all()
        left.delete()
        music = MusicRank1(title=name[0], artist=artists[0][0], cover_img=cover_img[0])
        music.save()

        # Send a message to #general channel
        slack.chat.post_message('C013UEVAZL0', 'Rank Changed')

musicChartCheck() # 한번 실행 하고
sched = BackgroundScheduler()
sched.add_job(musicChartCheck, 'interval', seconds=10) # 테스트로 10초에 한번씩
sched.start()
