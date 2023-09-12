import pytube
import os
import moviepy.editor as mp


def main():
    
    url = input("Enter Video URL: ")

    try:
        myvideo = pytube.YouTube(url)
    except pytube.exceptions.RegexMatchError:
        print("Error")
        exit()

    user_input1 = input('Video Or Mp3 (V / M): ').strip().capitalize()

    if user_input1 == 'V':
        stream=myvideo.streams.get_highest_resolution()
        stream.download(output_path=r"C:\Users\sohai\Videos")
    elif user_input1 == 'M':
        stream=myvideo.streams.filter(only_audio=True).first()
        stream.download(output_path=r"C:\Users\sohai\Music",filename=f"{myvideo.author}.mp4")
        
        mp4_file_path = r"C:\Users\sohai\Music\\" + f"{myvideo.author}" + ".mp4"
        mp3_file_path = r"C:\Users\sohai\Music\\" + f"{myvideo.author}" + ".mp3"
        
        audio_clip = mp.AudioFileClip(mp4_file_path)
        audio_clip.write_audiofile(mp3_file_path)
        
        audio_clip.close()
        os.remove(mp4_file_path)


if __name__ == "__main__":
    main()
