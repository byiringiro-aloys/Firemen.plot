import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Parameters
# -------------------------------------------------------------
v0 = 25.0            # initial speed (m/s)
g = 9.8              # gravitational acceleration (m/s^2)
x_target = 45.0      # horizontal distance to building (m)
t_hit = 3.0          # time of impact (s)

# -------------------------------------------------------------
# Derived quantities
# -------------------------------------------------------------
cos_a = x_target / (v0 * t_hit)
a = np.arccos(cos_a)
v0x = v0 * cos_a
v0y = v0 * np.sin(a)

# Trajectory curve
t = np.linspace(0, t_hit, 300)
x = v0x * t
y = v0y * t - 0.5 * g * t**2

# Impact point
y_hit = v0y * t_hit - 0.5 * g * t_hit**2

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))

plt.plot(x, y, linewidth=2.2, label="Water Trajectory")
plt.plot(0, 0, "o", color="green", markersize=9, label="Hose Exit")
plt.plot(x_target, y_hit, "s", color="red", markersize=9,
         label=f"Impact Point ({y_hit:.2f} m)")

plt.vlines(x_target, 0, y_hit, linestyle="--", color="gray", linewidth=2)
plt.axhline(0, color="sienna", linewidth=2)

plt.title(f"Projectile Path of Water Stream  (α = {np.degrees(a):.2f}°)",
          fontsize=15, weight="bold")
plt.xlabel("Horizontal Distance (m)", fontsize=12)
plt.ylabel("Vertical Height (m)", fontsize=12)

plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=11)
plt.axis("equal")
plt.ylim(bottom=0)

# Annotation for clarity
plt.annotate("Building Wall", xy=(x_target, y_hit),
             xytext=(x_target + 4, y_hit + 3),
             arrowprops=dict(arrowstyle="->", lw=1.5))

plt.annotate("Highest Point", 
             xy=(v0x * (v0y / g), (v0y**2) / (2 * g)),
             xytext=(v0x * (v0y / g) + 5, (v0y**2) / (2 * g) + 5),
             arrowprops=dict(arrowstyle="->", lw=1.5))

plt.tight_layout()
plt.show()