from flask import Flask, jsonify, request
import json
import os
1
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ AI 預測伺服器運行中！請使用 /predict.json"

@app.route('/predict.json')
def get_predict():
    if os.path.exists("predict.json"):
        with open("predict.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    else:
        return jsonify({"error": "predict.json 不存在"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # 接收 TradingView 的 alert 並回應處理
    print("收到 TradingView alert:", data)
    return 'received', 200
