from flask import Flask, jsonify
from src import analysis

app = Flask(__name__)


@app.route('/price_range/<c_name>', methods=['GET'])
def share_price_arr(c_name):
    analys = analysis(c_name)
    price_arr = analys.share_price_range('1mo', '1d')
    return jsonify(price_arr)

def add(a, b):
    return a+b

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)