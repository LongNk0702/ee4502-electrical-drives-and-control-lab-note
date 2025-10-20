import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

def build_dataset():
    # --- Exp1: sweep Duty Cycle ---
    exp1 = pd.DataFrame([
        {"DC(%)": 6.1,  "Speed(r/min)": 47,   "Torque(Nm)": 0.13},
        {"DC(%)": 48.2, "Speed(r/min)": 530,  "Torque(Nm)": 1.07},
        {"DC(%)": 93.7, "Speed(r/min)": 1127, "Torque(Nm)": 1.8},
    ])

    # --- Exp2: DC≈30%, vary load ---
    exp2 = pd.DataFrame([
        {"DC(%)": 30.2, "Speed(r/min)": 383, "Torque(Nm)": 0.01},
        {"DC(%)": 30.2, "Speed(r/min)": 290, "Torque(Nm)": 1.13},
        {"DC(%)": 30.2, "Speed(r/min)": 199, "Torque(Nm)": 1.80},
    ])

    # --- Exp3: DC≈50%, vary load ---
    exp3 = pd.DataFrame([
        {"DC(%)": 50.3, "Speed(r/min)": 663, "Torque(Nm)": 0.01},
        {"DC(%)": 50.3, "Speed(r/min)": 575, "Torque(Nm)": 1.08},
        {"DC(%)": 50.3, "Speed(r/min)": 208, "Torque(Nm)": 1.95},
    ])
    return exp1, exp2, exp3


# --- Load data ---
exp1, exp2, exp3 = build_dataset()

# --- Plot Torque (X) – Speed (Y) ---
plt.figure(figsize=(8,6))

plt.plot(exp1["Torque(Nm)"], exp1["Speed(r/min)"], 'o-', linewidth=2,
         label="Exp1 – Vary Duty (6.1–93.7%)")

plt.plot(exp2["Torque(Nm)"], exp2["Speed(r/min)"], 's--', linewidth=2,
         label="Exp2 – DC≈30% (Vary Load)")

plt.plot(exp3["Torque(Nm)"], exp3["Speed(r/min)"], 'd-.', linewidth=2,
         label="Exp3 – DC≈50% (Vary Load)")

plt.title("Speed vs Torque Characteristics (Exp1–Exp3)")
plt.xlabel("Torque (N·m)")
plt.ylabel("Speed (r/min)")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend(loc="best")

# --- Save figure ---
out_path = Path(f"exp1_2_3_speed_vs_torque_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
plt.savefig(out_path.as_posix(), dpi=300, bbox_inches="tight")
plt.show()

print("Saved:", out_path)
