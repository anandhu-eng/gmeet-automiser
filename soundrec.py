import sounddevice
from scipy.io.wavfile import write

fs=44100
sec=10
print("Recording.....")
rec_voice=sounddevice.rec(int(sec*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("output.wav",fs,rec_voice)


#for ubuntu, shoul install-- sudo apt-get install libportaudio2
#packages--- scipy and sounddevice