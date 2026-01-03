import numpy as np

def awgn_channel(signal, snr_db):
    """
    Add AWGN noise to a signal based on SNR in dB
    """
    # Signal power
    signal_power = np.mean(signal ** 2)

    # Convert SNR from dB to linear
    snr_linear = 10 ** (snr_db / 10)

    # Noise power
    noise_power = signal_power / snr_linear

    # Generate Gaussian noise
    noise = np.sqrt(noise_power) * np.random.randn(len(signal))

    # Received signal
    received_signal = signal + noise

    return received_signal
