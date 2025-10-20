import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# Data for Experiment 2
# Duty cycle 30.2%
torque_30 = [0.10, 1.13, 1.80]
speed_30 = [383, 290, 199]

# Duty cycle 50.3%
torque_50 = [0.01, 1.08, 1.95]
speed_50 = [663, 575, 208]

# Plot
plt.figure(figsize=(7,5))
plt.plot(torque_30, speed_30, 'o--', label='Duty Cycle = 30.2%')
plt.plot(torque_50, speed_50, 's--', label='Duty Cycle = 50.3%')

# Labels and title
plt.title('Torque–Speed Characteristics of DC Motor (Experiment 2)')
plt.xlabel('Torque (N·m)')
plt.ylabel('Speed (r/min)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# --- Save figure ---
out_path = Path(f"exp2_speed_vs_torque_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
plt.savefig(out_path.as_posix(), dpi=300, bbox_inches="tight")

# Show the plot
plt.show()

print(f"Figure saved to: {out_path.resolve()}")
