# foodbot
今日の気分や状況で食べたいものを決める食事を決めるのを悩んでめんどくさい方向けのchatbotアプリ。

## 処理概要
フロントエンドから入力されたメッセージをMeCabで形態素解析してキーワードを抽出する。
キーワードを辞書と比較して飲食店の検索パラメータを組み立てる。
グルメサーチAPIで検索パラメータを利用して飲食店を検索して候補リストを表示する。

## 環境
### フロントエンド
- react
- react-caht-element
- axios
### バックエンド
- python
- flask
- MeCab

## 環境構築
### 開発環境
ローカルPCの開発環境を構築する。

- Pythonとvscodeのインストール<br>
https://whitemarkn.com/learning-ai/visual-studio-code/
→Anacondaとvscodeのインストールをする。

- node.jsのインストール<br>
https://qiita.com/echolimitless/items/83f8658cf855de04b9ce

- MeCabのインストール<br>
https://qiita.com/menon/items/f041b7c46543f38f78f7

- Gitのインストール<br>
https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB

- ソースコードのクローン<br>
git clone https://github.com/takeiteasy810/foodbot.git

### バックエンド
#### 仮想環境を作成
vscodeのコマンドパレットからターミナルを開き以下のコマンドを実行。
```powershell
cd .\backend\
python -m venv env
```
#### 依存パッケージのインストール
コマンドパレットからインタープリタで仮想環境を選択。
コマンドパレットから新たにターミナルを開き以下のコマンドを実行。
```powershell
cd .\backend\
pip install -r requirements.txt
```

#### バックエンドの起動
コマンドパレットから以下のコマンドを実行。
```
python server.py
```

### フロントエンド
#### 依存パッケージのインストール
コマンドパレットから新たにターミナルを開き以下のコマンドを実行。
```powershell
cd .\frontend\app\
npm install --legacy-peer-deps
```
#### フロントエンドの起動
コマンドパレットから以下のコマンドを実行
```
npm start
```
