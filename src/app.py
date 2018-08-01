from os import path
import numpy as np
import config
from scipy.io.wavfile import read, write

from src import sound_operations
from src import pitch_detection

sample_rate, data = read(path.join(config.ROOT_DIR, "sounds", "a1.wav"))

'''Split wav file to channels'''
channel_count = len(data[0])
data = data.T
channels = []

for channel_number in np.arange(channel_count):
    channels.append(data[channel_number])

'''Check frequencies'''
pitch_detection.frequency_detection(channels[0], sample_rate)

# '''Shift pitch'''
# for shift in np.arange(-3, 3, step=1):
#     channels = []
#
#     for channel_number in np.arange(channel_count):
#         channels.append(data[channel_number])
#
#     for c in np.arange(len(channels)):
#         channels[c] = sound_operations.pitch_shift(sound_array=channels[c], n=shift)
#
#     '''Save modified channels to file'''
#     channels = np.array(channels).T
#     write(filename=path.join(config.ROOT_DIR, "output", str(shift) + "a.wav"), rate=sample_rate, data=channels)
