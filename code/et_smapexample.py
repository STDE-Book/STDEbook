import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
})

# Define the posterior distribution as a mixture of two Gaussians
p0, p1 = 0.98, 0.02  # Priors
m0, m1 = 4, 15       # Means
v0, v1 = 1.8, 0.0002    # Variances

s_values = np.linspace(0, 16, 10000)
posterior_mixture = (p0 * stats.norm.pdf(s_values, loc=m0, scale=np.sqrt(v0)) +
                     p1 * stats.norm.pdf(s_values, loc=m1, scale=np.sqrt(v1)))

# Find the MAP estimator (maximum of the posterior)
map_estimate = s_values[np.argmax(posterior_mixture)]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(7.5, 3))

# Plot the posterior distribution
ax.plot(s_values, posterior_mixture,
        label=r"Posterior distribution $p_{S|X}(s|x)$", linewidth=1)

# Append a custom tick for the MAP location
xticks = list(ax.get_xticks())                    # current x-tick positions
xticklabels = [f"{tick:g}" for tick in xticks]    # current x-tick labels
xticks.append(map_estimate)                       # add the MAP location
xticklabels.append(r"$\hat{s}_{{\rm MAP}}$")     # label it with LaTeX notation
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)

# Remove the y-tick position at the origin
yticks = list(ax.get_yticks())
yticks = [tick for tick in yticks if np.abs(tick) >= 0.0001]
ax.set_yticks(yticks)

# Remove the top and right spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Move the left spine to x=0 and the bottom spine to y=0 (optional)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Ticks on the 'bottom' and 'left' spines
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Adjust y-limits so y=0 is visible
y_max = 1.05 * posterior_mixture.max()
y_min = min(0, -0.01 * posterior_mixture.max())
ax.set_ylim([y_min, y_max])
ax.set_xlim([-0.5, 16])

# Labeling, legend, and grid
ax.set_xlabel("$s$")
ax.set_ylabel("$p_{S|X}(s|x)$")
# ax.set_title("MAP Estimator in a Mixture of Gaussians")
# ax.legend()
ax.grid(True, linestyle="dotted", alpha=0.5)


# Save the figure in a png file
plt.savefig("et_smapexample.png", dpi=300, bbox_inches='tight')
