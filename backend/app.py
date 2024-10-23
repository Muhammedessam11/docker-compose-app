# backend/app.py
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return "Hello from Flask and Docker Compose!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

