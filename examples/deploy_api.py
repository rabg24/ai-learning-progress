# Minimal Flask example to serve a local Hugging Face model for demo purposes
# Not production-ready. For demo only.

from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
nlp = pipeline("sentiment-analysis", model=MODEL)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    texts = data.get('texts')
    if not texts:
        return jsonify({'error': 'no texts provided'}), 400
    preds = nlp(texts)
    return jsonify(preds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
