import numpy as np
import matplotlib.pyplot as plt


def ar1_process(num_steps, num_realizations):
    # Initialize position at zero
    position = np.zeros((num_realizations,))
    # Initialize list of positions for each realization
    positions = np.zeros((num_steps, num_realizations))
    # Generate AR(1) process for num_steps steps and num_realizations
    # realizations
    for i in range(num_steps):
        e = np.random.normal(0, 1, (num_realizations,))
        position = 0.8 * position + e
        positions[i] = position
    return positions


nr = 1000
n_samples = 80
n_plots = 5
positions = ar1_process(n_samples, nr)

fig, axs = plt.subplots(
    nrows=n_plots + 1, ncols=1, sharex=True, sharey=True, figsize=(10, 6))

for i in range(n_plots):
    axs[i].stem(positions[:, i], use_line_collection=False)

mean_position = np.mean(positions, axis=0)
axs[n_plots].stem(mean_position, linefmt='C1-', markerfmt='C1o', basefmt='k-',
                  label='Mean of all realizations')

for i in range(n_plots + 1):
    if i < n_plots:
        axs[i].axhline(mean_position[i], color='C1', alpha=0.5)
        axs[i].text(positions.shape[0] + 3, mean_position[i],
                    f'{mean_position[i]:.3f}', va='center')
    else:
        mean_all = np.mean(positions)
        axs[i].axhline(mean_all, color='C1', alpha=0.5)
        axs[i].text(positions.shape[0] + 3, mean_all,
                    f'{mean_all:.3f}', va='center')

    # Hide subplot borders
    for spine in ['top', 'right']:
        axs[i].spines[spine].set_visible(False)
    axs[i].spines['bottom'].set_position('zero')


axs[n_plots].set_title('Mean of all realizations')
# axs[n_plots].legend()

plt.xlim([0, n_samples])
plt.tight_layout()
plt.savefig('sp_ergodicity.png')
plt.show()
