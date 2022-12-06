import subprocess
import os
from pathlib import Path

video_path = '/Users/linaliu/Movies/youtube/temp/'
file = "game"

def extract_audio(dir_path, filename):
    command = "ffmpeg -i " + dir_path + filename + " -ab 160k -ac 2 -ar 44100 -vn " + dir_path + file + ".wav"
    subprocess.call(command, shell=True)

def extract_audios(dir):
    os.chdir(dir)
    #paths = sorted(Path(dir).iterdir(), key=os.path.getmtime)
    paths = sorted(Path(dir).iterdir())
    print(paths)
    for myfile in paths:
        basename = os.path.basename(myfile)
        dirname = os.path.dirname(myfile)
        if 'DS_Store' in basename:
            continue
        if 'audio' in basename:
            continue
        print(basename)
        extract_audio(dir, basename)


extract_audios(video_path)