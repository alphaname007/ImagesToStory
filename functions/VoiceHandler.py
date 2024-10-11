import os
from gtts import gTTS


from functions.FileHandler import get_VoiceOverlay_Path


def generate_Voice_Overlays(sentences:list):
    for i, sentence in enumerate(sentences):
        voice_overlay = gTTS(sentence, lang="en")
        voice_overlay_path = os.path.join(get_VoiceOverlay_Path(), f"tmp_{i+1}.mp3")
        voice_overlay.save(voice_overlay_path)