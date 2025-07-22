import os
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Dictionnaire : label = nom dossier
EMOTIONS = {
    'happy': 0,
    'sad': 1,
    'angry': 2,
    'neutral': 3
}

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=3, offset=0.5)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

X, y = [], []

# Exemple : audio/happy/.wav, audio/sad/.wav, audio/angry/*.wav
for emotion, label in EMOTIONS.items():
    folder = f"audio/{emotion}"
    for file in os.listdir(folder):
        if file.endswith(".wav"):
            features = extract_features(os.path.join(folder, file))
            X.append(features)
            y.append(label)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(model, "model.pkl")
print("✅ Modèle entraîné et sauvegardé.")