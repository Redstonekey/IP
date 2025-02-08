from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    forwarded = request.headers.get('X-Forwarded-For')
    if forwarded:
        ip = forwarded.split(',')[0].strip()  # Take the first IP (client's real IP)
    else:
        ip = request.remote_addr  # Fallback if no proxy is used
    return ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
