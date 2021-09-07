import subprocess
vedio=''
audio=''
video_path=''
subprocess.run( "ffmpeg -y -i {vedio} -i {audio} -c:v copy -c:a aac -strict experimental " + video_path)
#subprocess.run( "ffmpeg -y -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental " + video_path)