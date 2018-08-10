import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
from src.sound_data import MIN_FREQUENCY, MAX_FREQUENCY


def frequency_detection(sound_array, sample_rate):
    min_shift, max_shift = get_shift_range(sample_rate, len(sound_array))

    shift = auto_correlation_analysis(sound_array, min_shift, max_shift)
    print(sample_rate, shift)
    print(sample_rate / shift)

    # cepstrum_analysis(sound_array, min_shift, max_shift)


def auto_correlation_analysis(sound_array, min_shift, max_shift):
    auto_correlation = []
    print(min_shift, max_shift)
    for shift in np.arange(min_shift, max_shift):
        auto_correlation.append(np.corrcoef(sound_array[:-shift], sound_array[shift:])[0, 1])

    shift_indices = np.arange(min_shift, max_shift)

    plt.xticks(np.arange(0, 2e4, 150))
    plt.plot(shift_indices, auto_correlation)
    plt.title("autocorrelation")
    plt.show()

    s = sorted(zip(auto_correlation, shift_indices))
    auto_correlation, shift_indices = map(list, zip(*s))

    return shift_indices[-1]


def partial_auto_correlation_analysis(sound_array, min_shift, max_shift):
    pass  # TODO


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
    minimal_shift = sample_rate // MAX_FREQUENCY
    maximum_shift = sample_rate // MIN_FREQUENCY

    if maximum_shift > max_length:
        maximum_shift = max_length

    return minimal_shift, maximum_shift
