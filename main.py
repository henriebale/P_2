import os, sys, subprocess, shlex, re
from subprocess import call
def probe_file(filename):
    cmnd = ['ffprobe', '-show_format', '-pretty', '-loglevel', 'quiet', filename]
    p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(filename)
    out, err = p.communicate()
    print("==========output==========")
    print(out)
    if err:
        print("========= error ========")
        print(err)

def change_resolution(filename,resolution):
    cmd="ffmpeg -i " + filename + " -vf scale="+resolution+" output.mp4"
    os.system(cmd)

ex="1"
while ex != "0":
    print("Exercice Nº (insert 0 to end)")
    ex=input()
    print(f"Exercise {ex} selected")
    if ex=="1":
        probe_file('BBB_video.mp4')
    elif ex=="2":
        os.rename('BBB_video_cut.mp4', 'BBB_1080.mp4')
        os.rename('BBB_video_720.mp4', 'BBB_720.mp4')
        os.rename('BBB_video_480.mp4', 'BBB_480.mp4')
        os.rename('BBB_video_240.mp4', 'BBB_240.mp4')
        os.rename('BBB_video_120.mp4', 'BBB_120.mp4')
    elif ex=="3":
        change_resolution('BBB_video.mp4','1280:720')
    elif ex=="4":
        os.system("ffmpeg -i BBB_video.mp4 -vcodec vp9 BBB_video_av.mp4")
    else:
        print(f"Exercise {ex} doesn't exiat")



