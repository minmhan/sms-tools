# Complex sinewave
# s[n] = exp(j2PIkn/N = Cos(2PIkn/N) + jSin(2PIkn/N)
import matplotlib.pyplot as plt
import numpy as np

N = 500
k = 3
n = np.arange(-N/2, N/2)
s = np.exp(1j * 2 * np.pi * k * n /N)

plt.plot(n, np.real(s))
plt.axis([-N/2, N/2-1, -1, 1])
plt.xlabel('n')
plt.ylabel('amplitude')

plt.show()
