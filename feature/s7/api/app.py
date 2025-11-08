from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
ERROR_COUNT = Counter('http_requests_errors_total', 'Total HTTP errors')
LATENCY = Histogram('http_request_duration_seconds', 'Request latency in seconds')

@app.route('/')
@LATENCY.time()
def index():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return "Hello from the API!"

@app.route('/slow')
@LATENCY.time()
def slow():
    REQUEST_COUNT.labels(method='GET', endpoint='/slow').inc()
    time.sleep(random.uniform(0.6, 1.2))
    return "This was slow..."

@app.route('/error')
@LATENCY.time()
def error():
    REQUEST_COUNT.labels(method='GET', endpoint='/error').inc()
    ERROR_COUNT.inc()
    return "Something went wrong!", 500

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
