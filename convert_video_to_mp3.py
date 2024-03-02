#--------------------Libraries-----------------
from pytube import YouTube
import os
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_youtube_url():
    speak("Please tell me the YouTube URL you'd like to play.")
    youtube_url = input("Enter the url: ")
    return youtube_url

def convert_video():
    print('\nYoutube to Mp3 Format Downloader\n')
    URL = get_youtube_url()
    yt = YouTube(URL)

    try:
        print("\nDownloading....")
        video = yt.streams.filter(only_audio=True).first()
        if video:
            out_file = video.download()
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
            speak("\nSuccessfully Downloaded\n")
            print(new_file)
            return new_file
        else:
            speak("\nVideo download failed.\n")

    except Exception as e:
        speak(f"\nError during video conversion: {e}\n")
if __name__ == "__main__":
    convert_video()