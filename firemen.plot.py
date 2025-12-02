import numpy as np
import matplotlib.pyplot as plt

# --- Given Parameters and Calculated Values ---
v0 = 25.0      # Initial speed (m/s)
g = 9.80       # Acceleration due to gravity (m/s^2)
x_building = 45.0  # Horizontal distance to building (m)
t_impact = 3.00  # Time of flight to building (s)

# Calculated values from part (a)
cos_alpha = 45.0 / (v0 * t_impact)
alpha_rad = np.arccos(cos_alpha)
alpha_deg = np.degrees(alpha_rad)
sin_alpha = np.sin(alpha_rad)

# Initial velocity components
v0x = v0 * cos_alpha
v0y = v0 * sin_alpha

# --- Trajectory Calculation ---
# Time array for plotting the full flight until the building
t_max = t_impact # We only plot until it hits the building
time = np.linspace(0, t_max, 100)

# Horizontal position: x(t) = v0x * t
x_t = v0x * time

# Vertical position: y(t) = v0y * t - 0.5 * g * t^2
y_t = v0y * time - 0.5 * g * time**2

# --- Plotting ---
plt.figure(figsize=(10, 6))

# Plot the trajectory
plt.plot(x_t, y_t, label='Water Stream Trajectory', color='blue')

# Mark the starting point (hose)
plt.plot(0, 0, 'o', label='Hose Exit', color='green', markersize=8)

# Mark the impact point (building)
y_impact = v0y * t_impact - 0.5 * g * t_impact**2
plt.plot(x_building, y_impact, 's', label=f'Impact Point\n(Height: {y_impact:.1f} m)', color='red', markersize=8)

# Draw the building as a vertical line
plt.vlines(x_building, 0, y_impact, linestyle='--', color='gray', label='Building Wall')

# Draw a line for the ground
plt.axhline(0, color='brown', linestyle='-', linewidth=2, label='Ground Level')

# Add labels and title
plt.title(f'Projectile Motion of Water Stream ($\\alpha = {alpha_deg:.1f}^\\circ$)', fontsize=14)
plt.xlabel('Horizontal Distance (x) [m]', fontsize=12)
plt.ylabel('Vertical Height (y) [m]', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.axis('equal') # Optional: Makes sure x and y axes have the same scale
plt.ylim(bottom=0) # Start the y-axis at 0

plt.show()