from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7540563843:AAEqNv4skbmYSHhep509PXqaNiCYCIEV8zM"
CHAT_ID = "5424649236"

@app.route('/', methods=['GET'])
def index():
    return 'Bot is running'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', 'No message received')

    send_telegram_message(message)
    return {'status': 'Message sent'}

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(debug=True)
