import numpy as np

def generate_bits(num_bits):
    """
    Generate random binary data (0s and 1s)
    """
    bits = np.random.randint(0, 2, num_bits)
    return bits
