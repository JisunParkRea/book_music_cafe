from slacker import Slacker
import os, sys, json
from django.core.exceptions import ImproperlyConfigured


# Get SLACK_BOT_TOKEN from secrets.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, 'secrets.json') # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SLACK_BOT_TOKEN = get_secret("SLACK_BOT_TOKEN")
slack = Slacker(SLACK_BOT_TOKEN)
slack.chat.post_message('C013UEVAZL0', 'test!!')