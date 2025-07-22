from flask import Flask, request, jsonify
from flask_cors import CORS
import librosa
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)
model = joblib.load("model.pkl")

def extract_features(file):
    y, sr = librosa.load(file, duration=3, offset=0.5)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

EMOTIONS = ['happy', 'sad', 'angry']

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Pas de fichier reçu'}), 400

    file = request.files['file']
    features = extract_features(file)
    prediction = model.predict([features])[0]
    emotion = EMOTIONS[int(prediction)]
    return jsonify({'emotion': emotion})

if __name__ == "__main__":
    app.run(debug=True)