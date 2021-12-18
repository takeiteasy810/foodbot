import requests
import json

url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
key = ''
format = 'json'


def kensaku(text):
    get_request = requests.get(url, params={
        'key': key,
        'keyword': text,
        'count': 1,
        'format': format})

    json_text = json.loads(get_request.text)
    print(json_text["results"]["shop"][0]["name"])
