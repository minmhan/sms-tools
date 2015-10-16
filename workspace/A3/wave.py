import numpy as np


t = np.arange(0,0.5,1.0/10000)
x1 = np.cos(2 * np.pi * 40 * t)
x2 = np.cos(2 * np.pi * 100 * t)
x3 = np.cos(2 * np.pi * 200 * t)
x4 = np.cos(2 * np.pi * 1000 * t)

x = x1 + x2 + x3 + x4

y1 = np.cos(2 * np.pi * 23 * t)
y2 = np.cos(2 * np.pi * 36 * t)
y3 = np.cos(2 * np.pi * 230 * t)
y4 = np.cos(2 * np.pi * 900 * t)
y5 = np.cos(2 * np.pi * 2300 * t)
y = y1 + y2 + y3 + y4 + y5
