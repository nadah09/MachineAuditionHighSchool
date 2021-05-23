from lib6003.audio import wav_read, wav_write, wav_play
import pyaudio
from math import sin, cos, pi, e
import matplotlib.pyplot as plt 
import synth_utils

j = 1j
fs = 22050

tune = [
    (369.99, 0.16666666666666666), (415.3, 0.16666666666666666),
    (440.0, 0.5), (369.99, 0.5), (369.99, 0.3333333333333333),
    (369.99, 0.16666666666666666), (369.99, 0.3333333333333333),
    (369.99, 0.3333333333333333), (329.63, 0.16666666666666666),
    (369.99, 0.3333333333333333), (369.99, 0.3333333333333333),
    (329.63, 0.16666666666666666), (329.63, 0.5),
    (246.94, 0.3333333333333333), (493.88, 0.3333333333333333),
    (246.94, 0.3333333333333333), (493.88, 0.3333333333333333),
    (369.99, 0.16666666666666666), (415.3, 0.16666666666666666),
    (440.0, 0.5), (369.99, 0.5), (369.99, 0.3333333333333333),
    (369.99, 0.16666666666666666), (369.99, 0.3333333333333333),
    (369.99, 0.3333333333333333), (329.63, 0.16666666666666666),
    (369.99, 0.3333333333333333), (369.99, 0.3333333333333333),
    (329.63, 0.16666666666666666), (329.63, 0.5),
    (246.94, 0.3333333333333333), (493.88, 0.3333333333333333),
    (246.94, 0.3333333333333333), (493.88, 0.6666666666666666),
    (277.18, 0.3333333333333333), (369.99, 0.3333333333333333),
    (415.3, 0.3333333333333333), (440.0, 0.3333333333333333),
    (415.3, 0.16666666666666666), (440.0, 0.16666666666666666),
    (415.3, 0.16666666666666666), (369.99, 0.16666666666666666),
    (415.3, 0.3333333333333333), (369.99, 0.3333333333333333),
    (277.18, 1.3333333333333333), (246.94, 1.1666666666666665),
    (277.18, 0.16666666666666666), (277.18, 0.3333333333333333),
    (369.99, 0.3333333333333333), (415.3, 0.3333333333333333),
    (440.0, 0.3333333333333333), (415.3, 0.6666666666666666),
    (369.99, 0.6666666666666666), (277.18, 1.3333333333333333),
    (246.94, 1.3333333333333333), (277.18, 0.3333333333333333),
    (369.99, 0.3333333333333333), (415.3, 0.3333333333333333),
    (440.0, 0.3333333333333333), (415.3, 0.16666666666666666),
    (440.0, 0.16666666666666666), (415.3, 0.16666666666666666),
    (369.99, 0.16666666666666666), (415.3, 0.3333333333333333),
    (369.99, 0.3333333333333333), (277.18, 1.3333333333333333),
    (246.94, 1.1666666666666665), (277.18, 0.16666666666666666),
    (277.18, 0.3333333333333333), (369.99, 0.3333333333333333),
    (415.3, 0.3333333333333333), (440.0, 0.3333333333333333),
    (415.3, 0.6666666666666666), (369.99, 0.6666666666666666),
    (277.18, 1.3333333333333333), (246.94, 1.3333333333333333),
    (277.18, 1.3333333333333333)]

samples = synth_utils.make_tune(tune, fs)
wav_play(samples,fs)
plt.plot(samples)
plt.show()

wav_play(samples,fs)