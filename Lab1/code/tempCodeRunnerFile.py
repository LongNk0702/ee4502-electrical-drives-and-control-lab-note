# --- Trục phải: Duty Cycle ---
# ax2 = ax1.twinx()  # <<== dòng này phải có trước khi gọi ax2
# ax2.plot(exp1["Speed(r/min)"], exp1["DC(%)"], 'k:', linewidth=1.5, label="Duty Cycle (%)")
# ax2.set_ylabel("Duty Cycle (%)", color='k')
# ax2.tick_params(axis='y', labelcolor='k')

# # --- Gộp legend từ cả 2 trục ---
# lines1, labels1 = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax1.legend(lines1 + lines2, labels1 + labels2, loc="best")