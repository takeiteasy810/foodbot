from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS
from utils import wakati, mainmain

app = Flask(__name__, static_folder="./build/static",
            template_folder="./build")
CORS(app)  # Cross Origin Resource Sharing


# トップ
@app.route("/", methods=['GET'])
def index():
    return "text parser:)"


# メイン
@app.route("/message", methods=['GET', 'POST'])
def parse():
    # print(request.get_json)
    # print(mainmain(request.get_json()))
    return make_response(
        jsonify(
            mainmain(request.get_json())
        )
    )


# サーバ
if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
