import numpy as np
from numpy.fft import fft, ifft
from scipy.interpolate import interp1d


def change_speed(sound_array: np.array, factor):
    if factor == 1:
        return np.array(sound_array, dtype=np.int16)

    if factor <= 0:
        raise ValueError('Illegal factor value')

    if factor > 1:
        indices = np.round(np.arange(0, len(sound_array), factor))
        indices = indices[indices < len(sound_array)].astype(int)
        return np.array(sound_array[indices.astype(int)], dtype=np.int16)

    if factor < 1:
        sound_interpolation = interp1d(x=np.arange(len(sound_array)), y=sound_array, kind="cubic")
        new_range = np.floor(np.arange((len(sound_array)), step=factor))
        new_sound = sound_interpolation(new_range)
        return np.array(new_sound, dtype=np.int16)


def stretch(sound_array, chunk, factor):
    # basically 3/4 of one chunk is overlapped with next chunk
    hop = chunk / 4
    phase = np.zeros(chunk)
    hanning = np.hanning(chunk)
    result = np.zeros(int(len(sound_array) / factor + chunk), dtype=complex)
    for i in np.arange(0, len(sound_array) - (chunk + hop), hop * factor):
        a1 = sound_array[int(i):int(i) + chunk]
        a2 = sound_array[int(i + hop):int(i + chunk + hop)]

        s1 = fft(hanning * a1)
        s2 = fft(hanning * a2)

        phase = (phase + np.angle(s1 / s2)) % 2 * np.pi
        a2_rephased = ifft(np.abs(s2) * np.exp(1j * phase))

        i2 = int(i / factor)
        result[i2:i2 + chunk] += hanning * a2_rephased
    result = ((2 ** (16 - 4)) * result / result.max())
    return np.int16(result)


def pitch_shift(sound_array, n, window_size=2 ** 13):
    factor = 2 ** (n / 12)
    stretched = stretch(sound_array=sound_array, chunk=window_size, factor=factor)
    return change_speed(stretched, 1 / factor)
