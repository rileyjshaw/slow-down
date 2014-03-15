import math
from numpy import *
import scipy.io.wavfile as wav

sine = lambda f, t, sr: math.sin(2 * math.pi * t * f / sr)

audio_rate, audio_data = wav.read('flute.wav')

def slowdown_keep_pitch_naive(chunk_size, song_data):
    temp_data = []
    for i in range(0, len(song_data), chunk_size):
        temp_data.extend([song_data[i + a] for a in range(chunk_size) if (i + a) < len(song_data)] * 2)
    return array(temp_data)

wav.write("really_naive.wav", audio_rate / 2, d)
wav.write("naive.wav", audio_rate, slowdown_keep_pitch_naive(1000, d))
