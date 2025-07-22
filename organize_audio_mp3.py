import os
import shutil

base_folder = "audio"
emotions = ['happy', 'sad', 'angry', 'neutral']

# Crée les sous-dossiers si besoin
for emotion in emotions:
    os.makedirs(os.path.join(base_folder, emotion), exist_ok=True)

# Déplace chaque mp3 dans le bon dossier selon le mot-clé dans le nom
for file in os.listdir(base_folder):
    if file.endswith(".mp3"):
        file_lower = file.lower()
        found = False
        for emotion in emotions:
            if emotion in file_lower:
                src = os.path.join(base_folder, file)
                dst = os.path.join(base_folder, emotion, file)
                shutil.move(src, dst)
                print(f"✔️ {file} déplacé dans {emotion}")
                found = True
                break
        if not found:
            print(f"❓ {file} n'a pas d'émotion détectée, non déplacé.")
