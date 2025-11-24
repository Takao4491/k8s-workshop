from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"service": "api", "ts": datetime.utcnow().isoformat()})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
