from flask import Flask
import threading
import time
import requests
from datetime import datetime

app = Flask(__name__)

# ================= CONFIG =================
ALIAS1_URL = "https://alias1.onrender.com/ping"
PING_INTERVAL = 3 * 60  # 3 minutes
# ==========================================


@app.route("/")
def home():
    return "Alias2 is running"


@app.route("/ping")
def ping():
    print_log("Received ping")
    return "pong from alias2"


def print_log(message):
    print(f"[{datetime.now()}] alias2 | {message}", flush=True)


def ping_alias1():
    while True:
        print_log("I am alive")

        try:
            requests.get(ALIAS1_URL, timeout=10)
            print_log("I called: alias1")
        except Exception as e:
            print_log(f"alias1 failed: {e}")

        time.sleep(PING_INTERVAL)


if __name__ == "__main__":
    threading.Thread(target=ping_alias1, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
