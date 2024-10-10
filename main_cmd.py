import os

from functions.FileHandler import *
from functions.Orchastrator import *


#main loop
def main():
    os.system('cls' if os.name=='nt' else 'clear')

    print(">> Images to Story <<")
    media_directory_path = input("Media-Folder: ")
    text = input("Story-Text: ")

    if (os.path.exists(media_directory_path)):
        print("\t> Ready to start generation")
        generate_Episode(media_directory_path, text)
    else:
         print("\t> I am sorry but this folder does not exist")

    input("Hit enter to continue")


if __name__ == "__main__":
    init()
    while True:
        main()