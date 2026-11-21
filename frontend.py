import os, threading, webbrowser
from flask import Flask, send_file, jsonify
import backend

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Create database.db and fill it with 500 rows on startup
backend.init_db()
backend.seed_big_data()

@app.route("/")
def home():
    p1 = os.path.join(BASE_DIR, "index.html")
    p2 = os.path.join(BASE_DIR, "templates", "index.html")
    return send_file(p1 if os.path.exists(p1) else p2)

# 2. View your database rows in the browser
@app.route("/api/records")
def records():
    return jsonify(backend.get_all_records())

if __name__ == "__main__":
    threading.Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:5050")).start()
    app.run(host="127.0.0.1", port=5050, debug=False)