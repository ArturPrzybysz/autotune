from os import path
import numpy as np
import config
from scipy.io.wavfile import read, write

from src import sound_data
from src.bpm_detector import get_bmp
from src.pitch_detection import frequency_detection
from src.pitch_shifting import adjust_frequency
from src.sound_data import find_closest_tone, get_tones_frequency

sampling_rate, sound = read(path.join(config.ROOT_DIR, "sounds", "test.wav"))

'''Split wav file to channels'''
channel_count = len(sound[0])
sound = np.array(sound).T

'''Detect bpm'''
bpm = get_bmp(np.array(sound[0][sampling_rate * 6:sampling_rate * 8]), sampling_rate)

'''Split channels to samples'''
sample_size = sound_data.get_sample_size(bpm, sampling_rate)
sample_count = sound.shape[1] // sample_size

sound2 = []

for c in np.arange(len(sound)):
    sound2.append(np.array(sound[c][:sample_size * sample_count]))

sound = np.reshape(np.array(sound2), (channel_count, sample_count, sample_size))
del sound2

'''Detect frequency in samples'''
frequencies = np.zeros((channel_count, sample_count))
for c in np.arange(channel_count):
    for s in np.arange(sample_count):
        frequencies[c][s] = frequency_detection(sound[c][s], sampling_rate)

'''Find closest tones to frequencies'''
closest_tone_frequency = np.zeros((channel_count, sample_count))
tones = get_tones_frequency()

for c in np.arange(channel_count):
    for s in np.arange(sample_count):
        closest_tone_frequency[c][s] = find_closest_tone(frequencies[c][s], tones)

'''Adjust frequencies to tones'''
for c in np.arange(channel_count):
    for s in np.arange(sample_count):
        tmp_sound = adjust_frequency(sound[c][s], frequencies[c][s], closest_tone_frequency[c][s])[:sample_size]
        sound[c][s] = tmp_sound

'''Detect frequency in samples'''
frequencies2 = np.zeros((channel_count, sample_count))
for c in np.arange(channel_count):
    for s in np.arange(sample_count):
        frequencies2[c][s] = frequency_detection(sound[c][s], sampling_rate)

'''Save wav file'''
sound = sound.reshape((channel_count, sample_count * sample_size)).T
write(path.join(config.ROOT_DIR, "output", "aac.wav"), sampling_rate, sound.astype("int16"))
