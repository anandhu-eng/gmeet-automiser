import subprocess
from multiprocessing import Process
from screeninfo import get_monitors
import sounddevice
from scipy.io.wavfile import write
#from soundrec import voice
l=[]
for i in get_monitors():
    i=str(i)
    l.append(i[8:-1])
for i in range(len(l)):
    l[i]=l[i].split(', ')
print(l)
monit=input("Enter the name of the monitor you are viewing from above list")
for i in range(len(l)):
    if(str(l[i][6])==("name="+"'"+str(monit)+"'")):
        print('yes')
        width=l[i][2][6:]
        height=l[i][3][7:]
def rec():
    subprocess.run("ffmpeg -f x11grab -s {width}x{height}  -r 25 -i :0.0+0,0  -fflags +igndts  -f pulse -async 25 -ac 1 -ar 44100 -i alsa_output.pci-0000_00_1f.3.analog-stereo.monitor  outq.mp4".format(width=width,height=height),shell=True)
rec()