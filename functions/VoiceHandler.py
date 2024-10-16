import os
from TTS.api import TTS
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(model_name=model_name)

from functions.FileHandler import get_VoiceOverlay_Path

def generate_Voice_Overlays(sentences:list):
    for i, sentence in enumerate(sentences):
        voice_overlay_path = os.path.join(get_VoiceOverlay_Path(), f"tmp_{i+1}.wav")
        tts.tts_to_file(text=sentence, file_path=voice_overlay_path)