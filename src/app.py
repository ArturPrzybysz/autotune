from os import path
import numpy as np
import config
from scipy.io.wavfile import read, write

from src import sound_data
from src import pitch_detection

sample_rate, data = read(path.join(config.ROOT_DIR, "sounds", "g1s.wav"))

'''Split wav file to channels'''
channel_count = len(data[0])
data = data.T
channels = []

for channel_number in np.arange(channel_count):
    channels.append(data[channel_number])

channels = np.array(channels)

'''Split channels to samples'''
sample_size = sound_data.get_sample_size(sample_rate)
channels = np.resize(channels, (channel_count, len(channels[0] // sample_size), sample_size))


'''Adjust samples frequency'''



# '''Check frequencies'''
# for channel_number in np.arange(channel_count):
#     pitch_detection.frequency_detection(channels[channel_number], sample_rate)

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
