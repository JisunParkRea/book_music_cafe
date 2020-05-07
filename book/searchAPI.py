import os, json
import sys
import urllib.request
from django.core.exceptions import ImproperlyConfigured


# Get CLIENT_ID, CLIENT_SECRET from secrets.json
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

client_id = get_secret("CLIENT_ID")
client_secret = get_secret("CLIENT_SECRET")

search_word = "파이썬" # 검색 단어
encText = urllib.parse.quote(search_word)
url = "https://openapi.naver.com/v1/search/book?query=" + encText +"&display=3&sort=count" # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)