import matplotlib.pyplot as plt
import numpy as np

def plot_bpsk(symbols):
    symbols = np.array(symbols)

    plt.figure()
    plt.stem(symbols)
    plt.title("BPSK Modulated Signal")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
import matplotlib.pyplot as plt

def plot_ber(snr_db, ber):
    plt.figure()
    plt.semilogy(snr_db, ber, marker='o')
    plt.title("BER vs SNR for BPSK over AWGN Channel")
    plt.xlabel("SNR (dB)")
    plt.ylabel("Bit Error Rate (BER)")
    plt.grid(True, which='both')
    plt.show()
