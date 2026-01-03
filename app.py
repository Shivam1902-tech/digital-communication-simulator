import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from bit_generator import generate_bits
from modulation import bpsk_modulate, qpsk_modulate
from channel import awgn_channel
from demodulation import bpsk_demodulate, qpsk_demodulate
from ber import calculate_ber

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Digital Communication Simulator",
    layout="centered"
)

# -------------------------------------------------
# Title & description
# -------------------------------------------------
st.title("📡 Digital Communication System Simulator")
st.subheader("BPSK / QPSK over AWGN Channel")

st.markdown("""
This simulator demonstrates **BPSK and QPSK modulation**
over an **Additive White Gaussian Noise (AWGN)** channel  
and evaluates system performance using **Bit Error Rate (BER)**.
""")

# -------------------------------------------------
# User inputs
# -------------------------------------------------
num_bits = st.slider(
    "Number of Bits (Single-SNR Simulation)",
    min_value=100,
    max_value=20000,
    step=100,
    value=5000
)

snr_db = st.slider(
    "SNR (dB)",
    min_value=0,
    max_value=15,
    step=1,
    value=5
)

modulation_type = st.radio(
    "Select Modulation Scheme",
    ("BPSK", "QPSK")
)

run = st.button("Run Simulation")

# -------------------------------------------------
# Simulation
# -------------------------------------------------
if run:
    st.markdown("---")
    st.header("📊 Simulation Results")

    # ---------------- SINGLE SNR SIMULATION ----------------
    bits = generate_bits(num_bits)

    if modulation_type == "BPSK":
        symbols = bpsk_modulate(bits)
        received = awgn_channel(symbols, snr_db)
        detected_bits = bpsk_demodulate(received)
    else:
        symbols = qpsk_modulate(bits)
        received = awgn_channel(symbols, snr_db)
        detected_bits = qpsk_demodulate(received)

    detected_bits = detected_bits[:len(bits)]
    ber = calculate_ber(bits, detected_bits)

    st.success("Simulation completed successfully!")
    st.write(f"### 📊 Bit Error Rate (BER): `{ber:.6f}`")

    # -------------------------------------------------
    # Received Signal Plot
    # -------------------------------------------------
    st.subheader("📈 Received Signal")

    fig1, ax1 = plt.subplots()

    if modulation_type == "BPSK":
        ax1.stem(np.real(received[:50]))
        ax1.set_xlabel("Sample Index")
        ax1.set_ylabel("Amplitude")
        ax1.set_title("BPSK Received Signal")
    else:
        ax1.scatter(
            np.real(received[:500]),
            np.imag(received[:500]),
            s=10
        )
        ax1.set_xlabel("In-phase (I)")
        ax1.set_ylabel("Quadrature (Q)")
        ax1.set_title("QPSK Constellation Diagram")
        ax1.set_xlim(-2, 2)
        ax1.set_ylim(-2, 2)
        ax1.axhline(0, color="gray", linewidth=0.5)
        ax1.axvline(0, color="gray", linewidth=0.5)

    ax1.grid(True)
    st.pyplot(fig1)

    # -------------------------------------------------
    # BER vs SNR Curve (ENGINEERING-CORRECT)
    # -------------------------------------------------
    st.subheader("📉 BER vs SNR Curve")

    snr_range = range(-2, 11, 2)
    ber_values = []

    BER_BITS = 100000  # 🔥 HIGH bit count for accurate BER

    for snr in snr_range:
        bits_ber = generate_bits(BER_BITS)

        if modulation_type == "BPSK":
            symbols_ber = bpsk_modulate(bits_ber)
            rx = awgn_channel(symbols_ber, snr)
            det = bpsk_demodulate(rx)
        else:
            symbols_ber = qpsk_modulate(bits_ber)
            rx = awgn_channel(symbols_ber, snr)
            det = qpsk_demodulate(rx)

        det = det[:len(bits_ber)]
        ber_val = calculate_ber(bits_ber, det)

        # Avoid log(0) — Monte Carlo floor
        if ber_val == 0:
            ber_val = 1 / BER_BITS

        ber_values.append(ber_val)

    fig2, ax2 = plt.subplots()
    ax2.semilogy(list(snr_range), ber_values, marker='o')
    ax2.set_xlabel("SNR (dB)")
    ax2.set_ylabel("Bit Error Rate (BER)")
    ax2.set_title(f"BER vs SNR for {modulation_type} over AWGN Channel")
    ax2.grid(True, which="both")

    st.pyplot(fig2)

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.markdown(
    "📘 **ECE Core Project** | Digital Communication System Simulator | Python + Streamlit"
)
