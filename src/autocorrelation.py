import numpy as np
from matplotlib import pyplot as plt


def find_max_correlation(sound_array, min_shift, max_shift, plot=False, correlation_step=1):
    auto_correlation = []
    for shift in np.arange(min_shift, max_shift, correlation_step):
        auto_correlation.append(np.corrcoef(sound_array[:-shift], sound_array[shift:])[0, 1])

    shift_indices = np.arange(min_shift, max_shift, correlation_step)

    if plot:
        plt.plot(shift_indices, auto_correlation)
        plt.title("autocorrelation")
        plt.show()

    s = sorted(zip(auto_correlation, shift_indices))
    auto_correlation, shift_indices = map(list, zip(*s))
    return shift_indices[-1]
