import os

def BASE_DIR():
    return os.getcwd()

def TMP_DIR():
    path = os.path.join(BASE_DIR(), ".tmp")
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def clear_TMP_DIR():
    #Clear VoiceOverlays
    for item in os.listdir(get_VoiceOverlay_Path()):
        item_path = os.path.join(get_VoiceOverlay_Path(), item)
        if os.path.isfile(item_path):
            os.remove(item_path)

def get_VoiceOverlay_Path():
    path = os.path.join(TMP_DIR(), "VoiceOverlays")
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def get_VoiceOverlay_Paths():
    voice_overlay_paths = [os.path.join(get_VoiceOverlay_Path(), file) for file in os.listdir(get_VoiceOverlay_Path()) if file.lower().endswith('.wav')]
    return sorted(voice_overlay_paths, key=lambda x: int(x.split('_')[1].split('.')[0]))

def get_Image_Paths(media_directory_path:str):
    return [os.path.join(media_directory_path, file) for file in os.listdir(media_directory_path) if file.lower().endswith('.jpg')]

def get_Outro_Path(media_directory_path:str):
    return os.path.join(media_directory_path, "outro.mp4")

def get_Music_Path(media_directory_path:str):
    return os.path.join(media_directory_path, "music.mp3")

def get_Output_Path(media_directory_path:str):
    return os.path.join(media_directory_path, "story.mp4")