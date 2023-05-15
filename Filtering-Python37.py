import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import butter, lfilter

def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
    b, a = butter(order,[lowcut, highcut], fs=fs, btype='band')
    y = lfilter(b, a, data)
    return y

def calculate(T, x, low_freq=50, high_freq=70, fs=600, order=2):
    """
    Parameters:
        T         =   Time in seconds that it would lasts the signal filtering
        x         =   Data to pass through the filter
        low_freq  =   Low cut frequency (Hz)
        high_freq =   High cut frequency (Hz)
        fs        =   Sampling Frequency or Sample Rate (Hz)
        order     =   Order complexity of the filter
    """
    nsamples = T * fs
    t = np.arange(0, nsamples)/fs

    y = butter_bandpass_filter(data=x, lowcut=low_freq, highcut=high_freq, fs=fs, order=order)
    return t, y

def time_calculate(T, fs):
    nsamples = T * fs
    t = np.arange(0, nsamples)/fs
    return t

def Manual_PS(Signal):
    dt = 1
    T = len(Signal) * dt
    x_freq = fft(Signal - np.mean(Signal))
    Sxx = 2 * dt ** 2 / T * (x_freq * np.conj(x_freq))
    #Sxx = Sxx[:int(len(Signal) / 2)]
    return Sxx

def Auto_PS(Signal):
    ps = np.abs(fft(Signal))**2
    return ps

def freq_step(Signal):
    freqs = fftfreq(len(Signal), 0.01)
    return freqs