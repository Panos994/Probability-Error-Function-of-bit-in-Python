import numpy as np
from scipy import special
import matplotlib.pyplot as plt

def inverse_qfunction(y):
    return np.sqrt(2) * special.erfinv(1 - 2 * y)

def calculate_SNRb(M, Pb):
    x = inverse_qfunction(Pb)
    SNRb = (M**2 - 1) / (2 * (M - 1) / (M * np.log2(M))) * x**2 / 6
    return 10 * np.log10(SNRb) #μετατροπη σε Db


M_values = [2**m for m in range(1, 11)]  # M = 2, 4, 8, ..., 1024
Pb_values = 10**(-6)  # Έστω Pb βάσει ΑΜ μου που τελειώνει σε 4 

# υπολογισμός του SNRb για κάθε M value
SNRb_values = [calculate_SNRb(M, Pb_values) for M in M_values]

# print  SNRb τιμές
for M, SNRb in zip(M_values, SNRb_values):
    print(f" for M={M}, calculate signal-to-noise per bit (SNRb) {SNRb:.2f} dB.") #se dB

# Plot tis grafikes parastaseis
custom_ticks = [0, 256, 512, 1024] #
plt.figure(figsize=(8, 6))
plt.plot(M_values, SNRb_values, marker='o', linestyle='-', color='b')
plt.xticks(custom_ticks, [str(M) for M in custom_ticks])  # deixno ta sigkekrimena ticks points poy thelo gia omoiomorfia
plt.xlabel('M PAM Class')
plt.ylabel('SNRb in dB')
plt.title(f'Calculated SNRb')
plt.grid(True)
plt.show()
