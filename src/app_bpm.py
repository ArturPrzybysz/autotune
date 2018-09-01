from os import path
import numpy as np
import config
from scipy.io.wavfile import read

from src.bpm_detector import get_bmp

sampling_rate, sound = read(path.join(config.ROOT_DIR, "sounds", "jack.wav"))

'''Split wav file to channels'''
channel_count = len(sound[0])
sound = sound.T

'''Detect bpm'''
bpm = get_bmp(np.array(sound[0][:60000]), sampling_rate)
bpm2 = get_bmp(np.array(sound[1][:60000]), sampling_rate)

print('BPM', bpm, bpm2)
