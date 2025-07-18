from flask import Flask, request, json, jsonify
from pyngrok import ngrok
import re

app = Flask(__name__)
port = 3000
public_url = ngrok.connect(port)
print("🚀 Public URL:", public_url , "/github-webhook")


@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    try:
        payload = request.get_data()
        # payload = unquote_plus(payload)
        # payload = re.sub('payload=', '', payload)
        payload = json.loads(payload)
        print(payload)
        return jsonify({"status": "Webhook received"}), 200
    except Exception as e:
        print("Error:", e)


if __name__ == '__main__':
    app.run(port=port)
    # github_webhook()
