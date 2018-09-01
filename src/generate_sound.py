from math import sin
from os import path

import numpy as np
from scipy.io.wavfile import write
from matplotlib import pyplot as plt

import config

sampling_rate = 44100
sound_time = 15
freq = 1000

sound = []

x = 0
overall_length = 0

for i in np.arange(0, 1.5, 0.000001):
    sound.append(sin(i * freq * np.pi * 2) * 10000)
    freq += 0.001

sound = np.array(sound).astype("int16")
sound = sound.reshape((len(sound) // 2, 2))

write(path.join(config.ROOT_DIR, "output", "test.wav"), sampling_rate, sound)
