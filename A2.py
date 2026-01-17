from flask import Flask
import threading
import time
import requests
from datetime import datetime

app = Flask(__name__)

# ================= CONFIG =================
A1_URL = "https://a1-y11o.onrender.com/ping"
PING_INTERVAL = 3 * 60  # 3 minutes
# ==========================================


@app.route("/")
def home():
    return "A2 is running"


@app.route("/ping")
def ping():
    print_log("Received ping")
    return "pong from A2"


def print_log(message):
    print(f"[{datetime.now()}] A2 | {message}", flush=True)


def ping_A1():
    while True:
        print_log("I am alive")

        try:
            requests.get(A1_URL, timeout=10)
            print_log("I called: A1")
        except Exception as e:
            print_log(f"A1 failed: {e}")

        time.sleep(PING_INTERVAL)


if __name__ == "__main__":
    threading.Thread(target=ping_A1, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)

