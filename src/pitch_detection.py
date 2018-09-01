import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
from numpy.ma import floor, ceil

from src.autocorrelation import find_max_correlation
from src.sound_data import MIN_FREQUENCY, MAX_FREQUENCY


def frequency_detection(sound_array, sampling_rate):
    min_shift, max_shift = get_shift_range(sampling_rate, len(sound_array))
    shift = find_max_correlation(sound_array, min_shift, max_shift)
    frequency = sampling_rate / shift

    return frequency


def cepstrum_analysis(sound_array, min_shift, max_shift):
    cepstrum = ifft(np.log(fft(sound_array)))
    ac = []
    shifts = []

    for shift in np.arange(min_shift, max_shift):
        ac.append(np.corrcoef(cepstrum[:-shift], cepstrum[shift:])[0, 1])
        ac.append(shift)

    plt.plot(shifts, ac)
    plt.title("cepstrum")
    plt.show()


def get_shift_range(sample_rate: int, max_length: int):
    """
    :param max_length: wav file data arrays length
    :param sample_rate: wav file sampling rate
    :return: shift range based on humans hearing frequency range (20Hz - 20kHz)
    """
    minimal_shift = int(ceil(sample_rate / MAX_FREQUENCY))
    maximum_shift = int(floor(sample_rate / MIN_FREQUENCY))

    if maximum_shift > max_length:
        maximum_shift = max_length

    return minimal_shift, maximum_shift
