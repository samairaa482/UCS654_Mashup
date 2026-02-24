import sys
import os
from yt_dlp import YoutubeDL
from moviepy.editor import AudioFileClip
from pydub import AudioSegment

DOWNLOAD_FOLDER="downloads"
AUDIO_FOLDER="audios"

os.makedirs(DOWNLOAD_FOLDER,exist_ok=True)
os.makedirs(AUDIO_FOLDER,exist_ok=True)


# -----------------------------
# Download Videos
# -----------------------------

def download_videos(singer,n):

    search = f"ytsearch{n}:{singer} songs"

    opts={

    "format":"bestaudio/best",

    "outtmpl":
    f"{DOWNLOAD_FOLDER}/%(id)s.%(ext)s"

    }

    with YoutubeDL(opts) as ydl:

        ydl.download([search])


# -----------------------------
# Convert to Audio
# -----------------------------

def convert_to_audio():

    for f in os.listdir(DOWNLOAD_FOLDER):

        video=os.path.join(
            DOWNLOAD_FOLDER,f)

        name=os.path.splitext(f)[0]

        audio_path=f"{AUDIO_FOLDER}/{name}.mp3"

        clip=AudioFileClip(video)

        clip.write_audiofile(audio_path)

        clip.close()


# -----------------------------
# Cut Audio
# -----------------------------

def cut_audio(duration):

    trimmed=[]

    for f in os.listdir(AUDIO_FOLDER):

        audio=AudioSegment.from_file(

            os.path.join(AUDIO_FOLDER,f))

        audio=audio[:duration*1000]

        trimmed.append(audio)

    return trimmed


# -----------------------------
# Merge
# -----------------------------

def merge_audio(clips,output):

    final=AudioSegment.empty()

    for c in clips:

        final+=c

    final.export(output,
                 format="mp3")



# -----------------------------
# MAIN
# -----------------------------

def main():

    if len(sys.argv)!=5:

        print(
"Usage: python file.py Singer Videos Duration Output")

        sys.exit()

    singer=sys.argv[1]
    videos=int(sys.argv[2])
    duration=int(sys.argv[3])
    output=sys.argv[4]

    if videos<10:

        print("Videos must >10")

        return

    if duration<20:

        print("Duration must >20")

        return

    try:

        download_videos(singer,videos)

        convert_to_audio()

        clips=cut_audio(duration)

        merge_audio(clips,output)

        print("Mashup created!")

    except Exception as e:

        print("Error:",e)



if __name__=="__main__":
    main()