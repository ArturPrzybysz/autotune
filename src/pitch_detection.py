import numpy as np
import matplotlib.pyplot as plt


def frequency_detection(sound_array, sample_rate):
    auto_correlation = []
    cepstrum = []
    shifts = []
    for shift in np.arange(1, len(sound_array) - 1):
        auto_correlation.append(np.corrcoef(sound_array[:-shift], sound_array[shift:])[0, 1])

        shifts.append(shift)

    plt.plot(shifts, auto_correlation)
    plt.show()
