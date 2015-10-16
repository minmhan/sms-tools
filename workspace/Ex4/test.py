import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft
import math
import matplotlib.pyplot as plt

M = 63
window = get_window('hanning', M)
hM1 = int(math.floor(M+1)/2)
hM2 = int(math.floor(M/2))

N = 512
hN = N/2
fftbuffer = np.zeros(512)
fftbuffer[:hM1] = window[hM2:]
fftbuffer[N-hM2:] = window[:hM2]

X = fft(fftbuffer)
absX = abs(X)
absX[absX < np.finfo(float).eps] = np.finfo(float).eps
mX = 20 * np.log10(absX)
pX = np.angle(X)

mX1 = np.zeros(N)
pX1 = np.zeros(N)
mX1[:hN] = mX[hN:]
mX1[N-hN:] = mX[:hN]
pX1[:hN] = pX[hN:]
pX1[N-hN:] = pX[:hN]

