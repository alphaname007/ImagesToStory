import random
import traceback


from functions.FileHandler import *
from functions.TextHandler import *
from functions.VoiceHandler import *
from functions.VideoHandler import *


def generate_Episode(media_directory_path:str, text:str):
    try:
        print("\t> started generation")

        print("extract sentences: ", end="")
        sentences = get_Sentences(text)
        print("☑")

        print("generate Voice-Overlays: ", end="")
        voice_overlay_paths = generate_Voice_Overlays(sentences)
        print("☑")

        print("generate Voice-Overlay-Clips: ", end="")
        voice_overlay_clips, voice_overlay_timestamps = generate_Voice_Overlay_Clips(voice_overlay_paths)
        print("☑")

        print("generate Text-Clips: ", end="")
        text_clips = generate_Text_Clips(sentences, voice_overlay_timestamps)
        print("☑")

        print("generate Image-Clips: ", end="")
        image_paths = get_Image_Paths(media_directory_path)
        random.shuffle(image_paths)
        image_clips = generate_Image_Clips(image_paths, voice_overlay_timestamps[-1])
        print("☑")

        print("render Episode-Video: ", end="")
        render_Episode(
            get_Outro_Path(media_directory_path),
            get_Music_Path(media_directory_path),
            image_clips,
            text_clips,
            voice_overlay_clips,
            voice_overlay_timestamps[-1],
            get_Output_Path(media_directory_path)
        )
        print("☑")
        
        return True, f"Successfully rendered {series_name}:{episode_name}"
    
    except Exception as e:
        traceback.print_exc()
        return False, f"could not render {series_name}:{episode_name} because of:{e}"
    
    finally:
        clear_TMP_DIR()