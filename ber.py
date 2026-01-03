import numpy as np

def calculate_ber(original_bits, detected_bits):
    """
    Calculate Bit Error Rate (BER)
    """
    errors = np.sum(original_bits != detected_bits)
    ber = errors / len(original_bits)
    return ber
