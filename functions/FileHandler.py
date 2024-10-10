import os

def BASE_DIR():
    return os.getcwd()

def TMP_DIR():
    if not os.path.exists(os.path.join(BASE_DIR(), ".tmp")):
        os.mkdir(os.path.join(BASE_DIR(), ".tmp"))
    return os.path.join(BASE_DIR(), ".tmp")

def clear_TMP_DIR():
    for filename in os.listdir(TMP_DIR()):
        file_path = os.path.join(TMP_DIR(), filename)
        os.remove(file_path)


def get_Image_Paths(media_directory_path:str):
    return [os.path.join(media_directory_path, file) for file in os.listdir(media_directory_path) if file.lower().endswith('.jpg')]

def get_Outro_Path(media_directory_path:str):
    return os.path.join(media_directory_path, "Outro.mp4")

def get_Music_Path(media_directory_path:str):
    return os.path.join(media_directory_path, "Music.mp3")

def get_Output_Path(media_directory_path:str):
    return os.path.join(media_directory_path, f"Story.mp4")