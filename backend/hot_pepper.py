import requests
import json

url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
key = ''
format = 'json'


def kensaku(text):
    if key == '':
        return 'Error : backend/hot_pepper.pyのKeyにAPIキーを入力してください'
    else:
        get_request = requests.get(url, params={
            'key': key,
            'keyword': text,
            'count': 1,
            'format': format})

        json_text = json.loads(get_request.text)
        # print(json_text)
        if json_text["results"]['results_available'] == 0:
            return '申し訳ございません。\n条件に引っかかるお店がありませんでした。'
        else:
            return json_text["results"]["shop"][0]["name"]
