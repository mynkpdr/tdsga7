# 23f3004197@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------------------
# Step 1: Generate Synthetic Data
# ----------------------------
np.random.seed(42)  # For reproducibility

# Define customer segments
segments = ['Budget', 'Regular', 'Premium', 'VIP']
data = []

# Simulate realistic purchase amounts per segment
for segment in segments:
    if segment == 'Budget':
        amounts = np.random.normal(loc=50, scale=15, size=150)
    elif segment == 'Regular':
        amounts = np.random.normal(loc=150, scale=30, size=200)
    elif segment == 'Premium':
        amounts = np.random.normal(loc=300, scale=50, size=120)
    else:  # VIP
        amounts = np.random.normal(loc=500, scale=100, size=80)
    
    # Clip negative values
    amounts = np.clip(amounts, a_min=0, a_max=None)
    
    # Append to data list
    data.extend([[segment, amt] for amt in amounts])

# Create DataFrame
df = pd.DataFrame(data, columns=['Customer Segment', 'Purchase Amount'])

# ----------------------------
# Step 2: Create Boxplot
# ----------------------------
sns.set_style("whitegrid")       # Professional style
sns.set_context("talk")          # Presentation-ready fonts

plt.figure(figsize=(8, 8))      # 512x512 pixels (dpi=64)

# Boxplot
sns.boxplot(
    x='Customer Segment',
    y='Purchase Amount',
    data=df,
    palette='Set2'
)

# Titles and labels
plt.title("Purchase Amount Distribution by Customer Segment", fontsize=16, weight='bold')
plt.xlabel("Customer Segment", fontsize=12)
plt.ylabel("Purchase Amount ($)", fontsize=12)

# ----------------------------
# Step 3: Save the chart
# ----------------------------
plt.savefig('chart.png', dpi=64, bbox_inches='tight')  # 512x512 pixels
plt.close()

print("Chart saved as chart.png")
