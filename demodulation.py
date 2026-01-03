import numpy as np

def bpsk_demodulate(received_signal):
    """
    Perform BPSK demodulation using hard decision
    """
    detected_bits = np.where(received_signal >= 0, 1, 0)
    return detected_bits
def qpsk_demodulate(received):
    """
    QPSK demodulation (hard decision)
    """
    I = np.real(received)
    Q = np.imag(received)

    bits_I = np.where(I >= 0, 1, 0)
    bits_Q = np.where(Q >= 0, 1, 0)

    bits = np.column_stack((bits_I, bits_Q)).flatten()
    return bits