from unittest import result
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
    json_text = hotPepperSearch(
        {
            'noun': noun['noun'],
            'gpsVaule': gpsVaule,
            'yoasobi': noun['yoasobi'],
            'osake': noun['osake']
        }
    )
    # 検索結果が0かどうか
    if 'error' in json_text["results"]:
        result['error'] = json_text["results"]['error'][0]['message']
    elif json_text["results"]['results_available'] == 0:
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
    # m = MeCab.Tagger('-Ochasen')
    # m = MeCab.Tagger('-Owakati')
    # m = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/ipadic')#normal ipadic辞書指定

    # x86 64Bit Intel系 AMD系 CPU
    # m = MeCab.Tagger(
    #     '-Ochasen -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')

    # ARM64(AArch64) 64Bit Apple_M系 Qualcomm_Snapdragon系 CPU
    m = MeCab.Tagger(
        '-Ochasen -d /usr/lib/aarch64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
    
    # m = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')

    # 解析結果
    hoge = m.parse(text)

    # 名詞だけを抽出
    lines = hoge.split('\n')
    noun = []  # 名詞が入っている
    yoasobi = False  # 深夜検索か
    osake = False  # お酒必須か

    for line in lines:
        feature = line.split('\t')
        if len(feature) > 2:  # 'EOS'と''を省く
            info = feature[3].split('-')
            # print(feature[0])
            # print(info)
            if info[0] in ('名詞'):
                if info[1] in ('一般'):
                    # print(feature[0])
                    # print(info)
                    noun.append(feature[0])
                if info[1] in ('副詞可能'):
                    if feature[0] == '深夜':
                        yoasobi = True
                if info[1] in ('固有名詞'):
                    noun.append(feature[0])
                    if feature[0] == 'お酒':
                        # print('お酒')
                        osake = True
    # 抽出した結果を返す
    return {'noun': noun, 'yoasobi': yoasobi, 'osake': osake}


def hotPepperSearch(data):
    # print(data)
    url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

    apiResult = ''  # レスポンス
    serchhoge = ''  # 検索文字
    gpsLatitude = ''  # 位置
    gpsLongitude = ''  # 位置
    midnight = ''  # 深夜営業
    midnight_meal = ''  # 深夜注文
    free_drink = ''  # 飲み放題
    cocktail = ''  # カクテル
    shochu = ''  # 焼酎
    sake = ''  # 日本酒
    wine = ''  # ワイン

    # 検索キーワード生成
    for noun in data['noun']:
        if noun == '久しぶり':
            print()
        elif noun == '雰囲気':
            print()
        elif noun == '気分':
            print()
        elif noun == '店':
            print()
        elif noun == '家':
            print()
        elif noun == '友達':
            print()
        else:
            serchhoge += noun + ' '

    # 位置情報
    if 'latitude' in data['gpsVaule']:
        gpsLatitude = data['gpsVaule']['latitude']
        gpsLongitude = data['gpsVaule']['longitude']

    #　深夜判定
    if 'yoasobi' in data:
        if data['yoasobi']:
            # print('深夜検索')
            midnight = 1
            midnight_meal = 1

    # お酒
    if 'osake' in data:
        if data['osake']:
            # print('お酒')
            free_drink = 1  # 飲み放題
            # cocktail = 1  # カクテル
            # shochu = 1  # 焼酎
            # sake = 1  # 日本酒
            # wine = 1  # ワイン

    # print('検索ワード')
    # print(serchhoge)

    # APIキーが有効化どうか判別
    if key == '':
        return 'Error : backend/hot_pepper.pyのKeyにAPIキーを入力してください'
    else:
        axiosResult = requests.get(url, params={
            'key': key,
            'keyword': serchhoge,
            'count': 1,
            'format': 'json',
            'lat': gpsLatitude,
            'lng': gpsLongitude,
            'range': 5,
            'midnight': midnight,
            'midnight_meal': midnight_meal,
            'free_drink': free_drink,
            'cocktail': cocktail,
            'shochu': shochu,
            'sake': sake,
            'wine': wine
        })
        apiResult = json.loads(axiosResult.text)

        # ヒットしない場合は全国で検索
        if apiResult["results"]['results_available'] == 0:
            # print('ヒット無し')
            # ヒット無し
            axiosResult = requests.get(url, params={
                'key': key,
                'keyword': serchhoge,
                'count': 1,
                'format': 'json',
                'midnight': midnight,
                'midnight_meal': midnight_meal,
                'free_drink': free_drink,
                'cocktail': cocktail,
                'shochu': shochu,
                'sake': sake,
                'wine': wine
            })
            apiResult = json.loads(axiosResult.text)

        # print(get_request.text)
        # 検索結果をJSON化して返す
        return apiResult
