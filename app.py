from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load a working, public model
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    headline = data.get('headline', '').strip()

    if not headline:
        return jsonify({"error": "Empty headline"}), 400

    result = classifier(headline)[0]
    label = result['label']
    confidence = round(result['score'] * 100, 2)

    # Interpret sentiment as real/fake approximation
    if label == "NEGATIVE":
        verdict = "Fake News"
        summary = "The headline seems exaggerated or misleading, similar to negative sentiment tone."
    else:
        verdict = "Real News"
        summary = "The headline appears neutral and factual, aligned with trustworthy news tone."

    return jsonify({
        "prediction": verdict,
        "confidence": confidence,
        "summary": summary
    })

if __name__ == '__main__':
    app.run(debug=True)
