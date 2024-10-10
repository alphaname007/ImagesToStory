import os
from gtts import gTTS


from functions.FileHandler import TMP_DIR


def generate_Voice_Overlays(sentences:list):
    voice_overlay_paths = []
    for i, sentence in enumerate(sentences):
        voice_overlay = gTTS(sentence, lang="en")
        voice_overlay_path = os.path.join(TMP_DIR(), f"tmp_{i+1}.mp3")
        voice_overlay.save(voice_overlay_path)
        voice_overlay_paths.append(voice_overlay_path)
    return voice_overlay_paths