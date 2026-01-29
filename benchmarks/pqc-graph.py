#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Data from test-data.tsv
labels = ['non-pqc', 'pqc']
x = np.arange(len(labels))
width = 0.6

# Handshakes data
handshakes_avg = [56835.5, 50805.9]
handshakes_err = [1157.926139, 2028.518039]

# Handshakes/s data
hps_avg = [3706.055, 3044.372]
hps_err = [67.69941117, 956.5243452]

# ---- Plot 1: Handshakes ----
plt.figure()
plt.bar(
    x,
    handshakes_avg,
    width,
    yerr=handshakes_err,
    capsize=5
)
plt.xticks(x, labels)
plt.ylabel('Handshakes')
plt.title('Average Handshakes with Standard Error')
plt.tight_layout()
plt.show()

# ---- Plot 2: Handshakes/s ----
plt.figure()
plt.bar(
    x,
    hps_avg,
    width,
    yerr=hps_err,
    capsize=5
)
plt.xticks(x, labels)
plt.ylabel('Handshakes per second')
plt.title('Average Handshakes/s with Standard Error')
plt.tight_layout()
plt.show()

