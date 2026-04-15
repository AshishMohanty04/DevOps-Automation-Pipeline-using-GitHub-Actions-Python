from flask import Flask, jsonify
import logging
from utils import process_data

app = Flask(__name__)

# Logging config
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

@app.route('/')
def home():
    logging.info("Home endpoint hit")
    return jsonify({"message": "DevOps Pipeline Running 🚀"})

@app.route('/process')
def process():
    result = process_data()
    logging.info("Data processed")
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)