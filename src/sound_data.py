import numpy as np

MAX_FREQUENCY = 2000
MIN_FREQUENCY = 50


def get_sample_size(bpm, sample_rate):
    beats_per_second = bpm / 60
    return int(sample_rate / (8 * beats_per_second))  # assuming we want to split every beat twice


def get_tones_frequency(a4_frequency=440):
    frequencies = []
    for n in range(-40, 50):
        frequencies.append(a4_frequency * 2 ** (n / 12))

    return frequencies


def find_closest_tone(frequency, tones):
    frequency = np.power(frequency, 2)
    tones = np.power(tones, 2)

    tone_idx = (np.abs(tones - frequency)).argmin()
    return np.power(tones, 1 / 2)[tone_idx]
