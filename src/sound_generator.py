import numpy as np


def _note(freq, length, amp=1, rate=44100):
    t = np.linspace(0, length, length * rate)
    data = np.sin(2 * np.pi * freq * t) * amp
    return data.astype("int16")


def generate_sound_by_freqs(frequencies, sample_size, sample_rate):
    sound = []
    for freq in frequencies:
        sound.append(_note(freq, sample_size, sample_rate))

    return np.array(sound)
