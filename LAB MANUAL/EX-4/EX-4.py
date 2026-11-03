import numpy as np
from scipy.linalg import hadamard
codes = hadamard(4)
data = np.array([1, -1, 1, -1])
signal = np.sum(data[:, None] * codes, axis=0)
print("Walsh Codes:\n", codes)
print("CDMA Signal:", signal)
print("Decoded Data:", np.sign(codes @ signal / 4))
