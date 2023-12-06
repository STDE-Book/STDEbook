import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)

# Define parameters for the walk
dims = 1
n_steps = 500
n_paths = 20
step_set = [-1, 1]

# Simulate steps in 1D
step_shape = (n_steps, dims)
origin = np.zeros((1, dims))

# Set figure
# plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
})
fig = plt.figure(figsize=(7.5, 3), dpi=200)
ax = fig.add_subplot(111)

# Plot bounds
ax.plot([0, n_steps], [0, n_steps], c='gray', lw=1)
ax.plot([0, n_steps], [0, -n_steps], c='gray', lw=1)

# Plot 2 standard deviations
time = np.arange(n_steps + 1)
std_line = 2 * np.sqrt(time)
# ax.plot(time, std_line, c='gray')
# ax.plot(-std_line, c='gray')
ax.fill_between(time, std_line, y2=-std_line, color='0.8')

for i in range(n_paths):

    steps = np.random.choice(a=step_set, size=step_shape)
    rw = np.concatenate([origin, steps]).cumsum(0)

    start = rw[:1]
    stop = rw[-1:]

    # Plot paths
    # ax.scatter(np.arange(n_steps + 1), rw, c='blue', alpha=0.25, s=5)
    # ax.plot(rw, c='blue', alpha=0.5, lw=10, ls='-',)
    ax.scatter(time, rw, c='blue', alpha=0.5, s=0.5, marker='.')
    ax.plot(rw, c='blue', alpha=0.9, lw=0.1)
    ax.plot(0, start, c='red', marker='+', markersize=1)
    ax.plot(n_steps, stop, c='black', marker='o', markersize=1)

ymax = 1.05 * np.sqrt(n_steps)
print(ymax)
ax.set_aspect('equal', 'box')
plt.title('Simple random walks')
plt.xlabel('$n$')
ax.set_ylabel('$X_n$')
# plt.axis('equal')
plt.xlim(0, n_steps)
plt.ylim(- 2.5 * ymax, 2.5 * ymax)
plt.tight_layout(pad=0)
plt.savefig('sp_random_walk_1d.png', dpi=250)
# plt.savefig('../Figures/sp_random_walk_1d.png', dpi=250)
plt.show(block=False)
