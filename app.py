# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_notification', methods=['POST'])
def send_notification():
    message = request.get_json()['message']
    print(f'Sending notification: {message}')
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    # Use SSL for local development
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=('cert.pem', 'key.pem'))
