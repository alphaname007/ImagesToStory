import os

from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

from functions.FileHandler import *
from functions.Orchastrator import *


#main loop
def main():
    os.system('cls' if os.name=='nt' else 'clear')

    print(">> Images to Story <<")
    media_directory_path = input("Media-Folder: ")
    text = input("Story-Text: ")

    print("\n\n\n")

    if (os.path.exists(media_directory_path)):
        print("Ready to start generation")
        generate_Episode(media_directory_path, text)
    else:
         print("I am sorry but this folder does not exist")

    print("\n")
    
    input("Hit enter to continue")


if __name__ == "__main__":
    while True:
        main()