import matplotlib.pyplot as plt
import numpy as np

# --- Dataset ---
quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
mrr_growth = [3.42, 3.68, 10.78, 10.78]
industry_target = 15.0

# --- Analysis ---
average_growth = np.mean(mrr_growth) # This will be 7.16

# --- Visualization ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the quarterly MRR growth
bars = ax.bar(quarters, mrr_growth, color=['#B0C4DE', '#B0C4DE', '#4682B4', '#4682B4'], label='Quarterly MRR Growth (%)')

# Plotting the industry target line
ax.axhline(y=industry_target, color='#FF6347', linestyle='--', linewidth=2, label=f'Industry Target ({industry_target}%)')

# Adding labels and title
ax.set_ylabel('MRR Growth (%)', fontsize=12)
ax.set_title('2024 Quarterly MRR Growth vs. Industry Target', fontsize=16, fontweight='bold')
ax.set_ylim(0, 18)

# Adding data labels on bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.3, f'{yval}%', ha='center', va='bottom')

# Adding a text box for the average
ax.text(0.95, 0.90, f'Average Growth: {average_growth:.2f}%',
        transform=ax.transAxes,
        fontsize=12,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', fc='aliceblue', alpha=0.8))

ax.legend()
plt.tight_layout()

# --- Save the plot ---
plt.savefig('mrr_growth_analysis.png', dpi=300)

print(f"Analysis complete. Average MRR Growth: {average_growth:.2f}")
print("Visualization saved as 'mrr_growth_analysis.png'")