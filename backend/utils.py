import requests
import json
import MeCab

# ホットペッパーグルメAPI Key
key = ''


# メイン
def mainmain(data):
    inputText = ''
    gpsVaule = ''
    result = {}

    # 入力テキスト
    if 'post_text' in data:
        inputText = data['post_text']
    # GPS位置情報
    gpsVaule = ''
    if 'gps_Value' in data:
        gpsVaule = data['gps_Value']
    # 形態素解析
    noun = wakati(inputText)
    # API検索
    json_text = hotPepperSearch({'noun': noun, 'gpsVaule': gpsVaule})
    # 検索結果が0かどうか
    if json_text["results"]['results_available'] == 0:
        result['error'] = '申し訳ございません。\n条件に引っかかるお店がありませんでした。'
    else:
        # お店の画像
        result['image'] = json_text["results"]["shop"][0]['photo']['pc']['l']
        # お店の名前
        result['shopName'] = json_text["results"]["shop"][0]["name"]
        # お店の紹介
        result['catch'] = json_text["results"]["shop"][0]['catch']
        # 営業時間
        result['open'] = json_text["results"]["shop"][0]['open']
        # お店のリンク
        result['url'] = json_text["results"]["shop"][0]["urls"]["pc"]
    # 結果
    return result


# 形態素解析
def wakati(text):
    # 解析する辞書
    m = MeCab.Tagger('-Ochasen')
    # m = MeCab.Tagger('-Owakati')
    # m = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/ipadic')#normal ipadic辞書指定
    # m = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')

    # 解析結果
    hoge = m.parse(text)

    # 名詞だけを抽出
    lines = hoge.split('\n')
    noun = []  # 名詞が入っている
    for line in lines:
        feature = line.split('\t')
        if len(feature) > 2:  # 'EOS'と''を省く
            info = feature[3].split('-')
            if info[0] in ('名詞'):
                # print(feature[0])
                noun.append(feature[0])

    # 抽出した名詞を返す
    return noun

# 検索文:  今日 久しぶり 彼女 デート 奮発 雰囲気 店 フレンチ
# 分解した言葉をAPIジャンル分け
# def recognition(nouns):
#     for noun in nouns:
#     if()


def hotPepperSearch(data):
    url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

    serchhoge = ''

    for noun in data['noun']:
        if(noun == 'フレンチ'):
            print('実行')
            serchhoge += noun

    # print(data)
    # APIキーが有効化どうか判別
    if key == '':
        return 'Error : backend/hot_pepper.pyのKeyにAPIキーを入力してください'
    else:
        get_request = ''
        if not data['gpsVaule']:
            # 通常検索
            get_request = requests.get(url, params={
                'key': key,
                'keyword': serchhoge,
                'count': 1,
                'format': 'json'
            })
        else:
            # 位置情報付き検索
            get_request = requests.get(url, params={
                'key': key,
                'keyword': serchhoge,
                'count': 1,
                'format': 'json',
                'lat': data['gpsVaule']['latitude'],
                'lng': data['gpsVaule']['longitude']
            })
        # print(get_request.text)
        # 検索結果をJSON化して返す
        return json.loads(get_request.text)
