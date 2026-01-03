import numpy as np

def bpsk_modulate(bits):
    """
    Perform BPSK modulation.
    0 -> -1
    1 -> +1
    """
    symbols = 2 * bits - 1
    return symbols
def qpsk_modulate(bits):
    """
    QPSK modulation with Gray coding and power normalization
    """
    if len(bits) % 2 != 0:
        bits = np.append(bits, 0)

    bit_pairs = bits.reshape(-1, 2)

    I = 2 * bit_pairs[:, 0] - 1
    Q = 2 * bit_pairs[:, 1] - 1

    symbols = (I + 1j * Q) / np.sqrt(2)  # 🔥 NORMALIZATION
    return symbols
