from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/react', methods=['POST'])  
def react():
    if request.method == 'POST':
        
        reaction = request.form.get('selected_reaction')
        post_link = request.form.get('post_link')
        cookies = request.form.get('cookies')

        
        if post_link is None or reaction is None:
            return jsonify({"status": "error", "message": "Missing required parameters"}), 400

        
        data = {
            "post_id": post_link,
            "react_type": reaction
        }

        
        headers = {
            "Cookie": cookies,
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; Plume L2 Build/O00623)",
            "Host": "flikers.net",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "Content-Length": "0"
        }

        
        res = requests.post('https://flikers.net/android/android_get_react.php', json=data, headers=headers).json()

        
        if res['status'] == 'SUCCESS':
            msg = res['message']
            return jsonify({"status": "success", "message": msg}), 200
        else:
            msg = res['message']
            return jsonify({"status": "error", "message": msg}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
