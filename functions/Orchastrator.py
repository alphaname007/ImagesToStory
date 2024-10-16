import random
import traceback


from functions.FileHandler import *
from functions.TextHandler import *
from functions.VoiceHandler import *
from functions.VideoHandler import *


def generate_Episode(media_directory_path:str, text:str):
    try:
        clear_TMP_DIR()
        print("\t> started generation")

        print("\t> extract sentences: ", end="")
        sentences = get_Sentences(text)
        print("☑")

        print("\t> generate Voice-Overlays: ", end="")
        generate_Voice_Overlays(sentences)
        print("☑")

        print("\t> generate Voice-Overlay-Clips: ", end="")
        voice_overlay_paths = get_VoiceOverlay_Paths()
        voice_overlay_clips, voice_overlay_timestamps = generate_Voice_Overlay_Clips(voice_overlay_paths)
        print("☑")

        print("\t> generate Text-Clips: ", end="")
        text_clips = generate_Text_Clips(sentences, voice_overlay_timestamps)
        print("☑")

        print("\t> generate Image-Clips: ", end="")
        image_paths = get_Image_Paths(media_directory_path)
        random.shuffle(image_paths)
        image_clips = generate_Image_Clips(image_paths, voice_overlay_timestamps[-1])
        print("☑")

        print("\t> render Episode-Video: ", end="")
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
        
        return True, f"Successfully rendered"
    
    except Exception as e:
        traceback.print_exc()
        return False, f"could not render because of:{e}"

    finally:
        pass