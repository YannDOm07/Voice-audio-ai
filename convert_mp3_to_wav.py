from pydub import AudioSegment
import os

mp3_base = "raw_audio_mp3"  # ton dossier contenant les .mp3 (à renommer si besoin)
wav_base = "audio"          # dossier de sortie (.wav), utilisé par train_model.py

EMOTIONS = ['happy', 'sad', 'angry', 'neutral']

for emotion in EMOTIONS:
    input_folder = os.path.join(mp3_base, emotion)
    output_folder = os.path.join(wav_base, emotion)
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".mp3"):
            mp3_path = os.path.join(input_folder, file)
            wav_path = os.path.join(output_folder, file.replace(".mp3", ".wav"))

            sound = AudioSegment.from_mp3(mp3_path)
            sound.export(wav_path, format="wav")
            print(f"✔️ {file} converti → {wav_path}")