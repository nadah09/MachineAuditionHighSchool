from lib6003.audio import wav_read, wav_write, wav_play
import pyaudio
from math import sin, cos, pi, e
import matplotlib.pyplot as plt 

def make_tune(tune, fs):
    """
    Constructs wav file samples from frequency, duration list of notes and sampling rate
    """
    samples = []
    for freq, duration in tune:
        period += duration
        f = freq
        seconds = duration
        Omega = 2*pi*f/fs
        for n in range(int(seconds*fs)): # TODO: how many samples should we generate?
            samples.append(sin(Omega*n))
            
    plt.plot(samples)
    plt.show()