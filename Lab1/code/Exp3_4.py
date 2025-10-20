import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# --- Data from Experiments 3 & 4 ---
data = {
    "Field Current (mA)": [150, 200, 270, 150, 150, 150, 300, 300, 300],
    "Condition": [
        "No Load (Exp.3)", "No Load (Exp.3)", "No Load (Exp.3)",
        "Loaded (Exp.4, If=150)", "Loaded (Exp.4, If=150)", "Loaded (Exp.4, If=150)",
        "Loaded (Exp.4, If=300)", "Loaded (Exp.4, If=300)", "Loaded (Exp.4, If=300)"
    ],
    "Torque (N·m)": [0.01, 0.01, 0.01, 0.01, 1.08, 1.95, 0.01, 1.12, 1.95],
    "Speed (r/min)": [953, 789, 661, 956, 89, 95, 669, 564, 216]
}

# Create DataFrame
df = pd.DataFrame(data)

# Separate data by field current
df_150 = df[df["Field Current (mA)"] == 150]
df_300 = df[df["Field Current (mA)"] == 300]

# --- Plot ---
plt.figure(figsize=(7,5))
plt.plot(df_150["Torque (N·m)"], df_150["Speed (r/min)"], 'o--', label='Field Current = 150 mA')
plt.plot(df_300["Torque (N·m)"], df_300["Speed (r/min)"], 's--', label='Field Current = 300 mA')

plt.title('Torque–Speed Characteristics for Two Field Currents (Experiments 3 & 4)')
plt.xlabel('Torque (N·m)')
plt.ylabel('Speed (r/min)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# --- Save figure ---
out_path = Path(f"exp3_4_torque_speed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
plt.savefig(out_path.as_posix(), dpi=300, bbox_inches="tight")
plt.show()

print(f"Figure saved to: {out_path.resolve()}")
