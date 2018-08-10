MAX_FREQUENCY = 2500
MIN_FREQUENCY = 60


def get_sample_size(sample_rate):
    return sample_rate / MIN_FREQUENCY


def get_tones_frequency(a4_frequency=440):
    frequencies = []
    for n in range(-50, 50):
        frequencies.append(a4_frequency * 2 ** (n / 12))

    return frequencies
