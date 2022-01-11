import json
import os
from flask import Flask,jsonify,request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# @app.route("/price/", methods=['GET'])
# def return_price():
#     date = request.args.get('date')
#     month = request.args.get('month')
#     year = request.args.get('year')
#     price = my_bitcoin_predictor.predict(date, month, year)
#     price_dict = {
#         'model': 'mlp',
#         'price': price,
#         }
#     return jsonify(price_dict)


@app.route("/", methods=['GET'])
def default():
    return "<h1> Welcome to bitcoin price predictor <h1>"


if __name__ == "__main__":
    app.run()
