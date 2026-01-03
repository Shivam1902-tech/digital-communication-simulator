import numpy as np
from bit_generator import generate_bits
from modulation import bpsk_modulate
from channel import awgn_channel
from demodulation import bpsk_demodulate
from ber import calculate_ber

snr_range = range(0, 11, 2)  # 0 to 10 dB
ber_values = []

bits = generate_bits(10000)
symbols = bpsk_modulate(bits)

for snr_db in snr_range:
    received = awgn_channel(symbols, snr_db)
    detected_bits = bpsk_demodulate(received)
    ber = calculate_ber(bits, detected_bits)
    ber_values.append(ber)
    print(f"SNR = {snr_db} dB, BER = {ber}")
from plots import plot_ber
plot_ber(list(snr_range), ber_values)
