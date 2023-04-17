# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:35:10 2023

@author: Gbenga Agunbiade
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters for the non-Gaussian distribution
mu = 5    # Mean
sigma = 2  # Standard deviation

# Number of experiments
M = 10000

# Sample sizes to consider
N_values = [1, 5, 10, 50]

# Generate samples and compute averages for each sample size
for N in N_values:
    averages = np.zeros(M)  # Array to store the computed averages

    for i in range(M):
        samples = np.random.normal(mu, sigma, N)  # Generate N samples from the non-Gaussian distribution
        averages[i] = np.mean(samples)           # Compute the average of the N samples

    # Plot the distribution of averages
    plt.hist(averages, bins=30, density=True, alpha=0.5, label=f'N = {N}')  # Histogram of averages

# Plot the Gaussian distribution with the same mean and standard deviation
x = np.linspace(mu - 5*sigma, mu + 5*sigma, 100)
y = (1/(sigma * np.sqrt(3 * np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)
plt.plot(x, y, color='purple', label='Gaussian')

# Add labels and legend to the plot
plt.xlabel('Averages')
plt.ylabel('Density')
plt.title('Central Limit Theorem')
plt.legend()
plt.show()