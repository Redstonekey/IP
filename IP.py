from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def get_ip():
    forwarded = request.headers.get('X-Forwarded-For')
    if forwarded:
        ip = forwarded.split(',')[0].strip()
    else:
        ip = request.remote_addr
    
    return render_template('index.html', ip=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
