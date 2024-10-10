from moviepy.editor import ImageClip, TextClip, AudioFileClip, VideoFileClip, ColorClip, CompositeVideoClip, CompositeAudioClip

from functions.TextHandler import combined_Words


def generate_Voice_Overlay_Clips(voice_overlay_paths:list):
    voice_overlay_timestamps = [0]
    count_time = 0
    voice_overlay_clips = []
    for i, voice_overlay_path in enumerate(voice_overlay_paths):
        voice_overlay_clip = AudioFileClip(voice_overlay_path)
        count_time += voice_overlay_clip.duration
        voice_overlay_timestamps.append(count_time)
        voice_overlay_clip = voice_overlay_clip.set_start(voice_overlay_timestamps[i])
        voice_overlay_clips.append(voice_overlay_clip)
    return voice_overlay_clips, voice_overlay_timestamps


def zoom_Value(t):
    return 1 + 0.2 * t #zomm factor 0.2

def generate_Image_Clips(image_paths:list, duration:float):
    image_clips = []
    count_image_clips = int(duration / 3)
    duration_last_image_clip = duration % 3
    for i in range(count_image_clips + 1):
        image_clip = ImageClip(image_paths[i % len(image_paths)])
        image_clip = image_clip.set_start(i * 3)
        image_clip = image_clip.set_duration(3 if i < count_image_clips + 1 else duration_last_image_clip)
        image_clip = image_clip.set_fps(24)
        image_clip = image_clip.set_position(('center', 'center'))
        image_clip = image_clip.resize(width=1.8*1920, height=1.8*1080)
        image_clip = image_clip.resize(zoom_Value)
        image_clips.append(image_clip)
    return image_clips


def generate_Text_Clips(sentences:list, voice_overlay_timestamps:list, color="white", bg_color="black"):
    text_clips = []
    for i, sentence in enumerate(sentences):
        sentence_words = sentence.split(" ")
        sentence_words = list(filter(lambda x: x != "", sentence_words))
        combined_words = combined_Words(sentence_words)

        all_combined_words_duration = voice_overlay_timestamps[i+1] - voice_overlay_timestamps[i]
        combined_words_duration = all_combined_words_duration / len(combined_words)
        for j, combined_sentence_word in enumerate(combined_words):
            text_clip = TextClip(" "+combined_sentence_word+" ", fontsize=80, color=color, bg_color=bg_color, font="Maxima")
            text_clip = text_clip.set_position(('center', 1700))
            text_clip = text_clip.set_start(voice_overlay_timestamps[i] + j * combined_words_duration)
            text_clip = text_clip.set_duration(combined_words_duration)
            text_clips.append(text_clip)
    return text_clips


def render_Episode(outro_path:str, music_path:str, image_clips, text_clips, voice_overlay_clips, duration:float, output_path:str):
    outro_clip = VideoFileClip(outro_path)
    outro_clip = outro_clip.set_start(duration)
    outro_clip = outro_clip.set_position(('center', 'center'))

    music_clip = AudioFileClip(music_path)
    music_clip = music_clip.set_start(0)
    music_clip = music_clip.set_duration(duration + outro_clip.duration)
    music_clip = music_clip.volumex(0.4)

    empty_clip = ColorClip(size=(1080, 1920), color=(0.0, 0.0, 0.0))
    empty_clip = empty_clip.set_fps(24)
    empty_clip = empty_clip.set_start(0)
    empty_clip = empty_clip.set_duration(duration + outro_clip.duration)

    background_clip = ColorClip(size=(950, 1870), color=(0.0, 0.0, 0.0))
    background_clip = background_clip.set_fps(24)
    background_clip = background_clip.set_duration(duration)
    background_clip = background_clip.set_position(('center', 'center'))

    all_clips = [empty_clip] + image_clips + [outro_clip] + text_clips
    audio = CompositeAudioClip(voice_overlay_clips + [music_clip])

    episode_video = CompositeVideoClip(all_clips)
    episode_video = episode_video.set_fps(24)
    episode_video = episode_video.set_audio(audio)
    episode_video = episode_video.set_end(duration + outro_clip.duration)
    episode_video.write_videofile(output_path, codec='libx264', audio_codec='aac',)
    return True