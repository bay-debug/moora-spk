import streamlit as st
import numpy as np

from pyDecision.algorithm import moora_method

# MOORA
st.write('Hasil Perangkingan dengan Metode MOORA')

# Weights
weights = [0.45, 0.25, 0.15, 0.1, 0.05]

# Load Criterion Type: 'max' or 'min'
criterion_type = ['min', 'max', 'max', 'min', 'max']

# Dataset
dataset = np.array([
    [90, 80, 80, 70, 90],   #a1
    [70, 80, 70, 70, 90],   #a2
    [80, 80, 70, 90, 80],   #a3
    [70, 70, 90, 90, 80],   #a4
    [70, 90, 90, 90, 80],   #a5

])

# Call MOORA Function
rank = moora_method(dataset, weights, criterion_type, graph=True, verbose=True)

# Menampilkan hasil perangkingan ke dalam antarmuka Streamlit
st.write('Hasil Perangkingan:')
st.write(rank)
