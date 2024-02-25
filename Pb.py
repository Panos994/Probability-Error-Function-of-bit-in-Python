import numpy as np
from scipy import special
import matplotlib.pyplot as plt

def inverse_qfunction(y): # η αντίστροφη συνάρτηση 
    return np.sqrt(2) * special.erfinv(1 - 2 * y)

def calculate_SNRb(M, Pb): #λύνουμε ως προς SNRb
    x = inverse_qfunction(Pb)
    SNRb = (M**2 - 1) / (2 * (M - 1) / (M * np.log2(M))) * x**2 / 6
    return 10 * np.log10(SNRb) #μετατροπη σε Db
