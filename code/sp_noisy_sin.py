import numpy as np
import matplotlib.pyplot as plt

# Define sample size
n = 60
n_plots = 4

# Generate 5 realizations of the stochastic process
fig, axs = plt.subplots(
    nrows=n_plots, ncols=1, sharex=True, sharey=True, figsize=(10, 6))

for i in range(4):
    # Generate independent samples for each realization
    loc = 4 * np.sin(np.pi / 20 * (np.arange(0, n)))
    scale = np.abs(loc)
    X = np.random.normal(loc=loc, scale=scale)

    # Plot each realization in a subplot
    axs[i].stem(X, use_line_collection=False)

    # Hide subplot borders
    for spine in ['top', 'right']:
        axs[i].spines[spine].set_visible(False)

    axs[i].spines['bottom'].set_position('zero')

    # Show only x and y axes
    axs[i].xaxis.set_ticks_position('bottom')
    axs[i].yaxis.set_ticks_position('left')
    axs[i].tick_params(axis='x', direction='out', width=1, length=3)
    axs[i].tick_params(axis='y', direction='out', width=1, length=3)

# Configure the plot
plt.xlim([0, n])
plt.tight_layout()

# Save the figure to a png file
plt.savefig('sp_noisy_sin.png')

plt.show()
