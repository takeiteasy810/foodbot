import MeCab
from hot_pepper import kensaku

def wakati(text):
    '''分かち書き用関数
    input  << text : 入力テキスト
    output >> m.parse(wakatext) : 分かち済みテキスト'''
    wakatext = text
    m = MeCab.Tagger('-Ochasen')
    #m = MeCab.Tagger('-Owakati')
    #m = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/ipadic')#normal ipadic辞書指定
    hoge = m.parse(wakatext)

    lines = hoge.split('\n')
    search = ''
    for line in lines:
        feature = line.split('\t')
        if len(feature) > 2:  # 'EOS'と''を省く
            info = feature[3].split('-')
            if info[0] in ('名詞'):
                print(feature[0])
                search += feature[0] + ' '
    print('検索文: ', search)
    tenmei = kensaku(search) + '\n 検索文字「' + search + '」'
    return tenmei
