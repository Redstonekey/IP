from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    forwarded = request.headers.get('X-Forwarded-For')
    if forwarded:
        ip = forwarded.split(',')[0].strip()
    else:
        ip = request.remote_addr
    
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your IP Address</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-size: 50px;
                font-family: Arial, sans-serif;
            }}
        </style>
    </head>
    <body>
        {ip}
    </body>
    </html>'''
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
