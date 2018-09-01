import numpy as np

from src.autocorrelation import find_max_correlation

MAX_BPM_FREQUENCY = 2.5
MIN_BPM_FREQUENCY = 0.8


def _get_shift_range(sampling_rate: int):
    minimal_shift = int(np.ceil(sampling_rate / MAX_BPM_FREQUENCY))
    maximum_shift = int(np.floor(sampling_rate / MIN_BPM_FREQUENCY))
    return minimal_shift, maximum_shift


def get_bmp(audio_array: np.array, sampling_rate: int):
    lowest_shift, highest_shift = _get_shift_range(sampling_rate)

    best_shift = find_max_correlation(audio_array, lowest_shift, highest_shift, False, correlation_step=300)
    bps = sampling_rate / best_shift
    bpm = bps * 60

    return bpm
