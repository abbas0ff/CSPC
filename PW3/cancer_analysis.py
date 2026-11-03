import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# 1. Load dataset
df = pd.read_csv('chemicals_cancer.csv')
print("Shape:", df.shape)
target_col = [c for c in df.columns if 'malignancy' in c or 'tumor' in c][0]
r_b_naive, p_b = stats.pearsonr(df['benzene'], df[target_col])
r_c_naive, p_c = stats.pearsonr(df['cadmium'], df[target_col])
print("\n--- Task 6: Naive Correlations ---")
print(f"Benzene vs Malignancy: r = {r_b_naive:.4f}")
print(f"Cadmium vs Malignancy: r = {r_c_naive:.4f}")
p_low = df['pollution_index'].quantile(0.4)
p_high = df['pollution_index'].quantile(0.6)
mask = (df['pollution_index'] >= p_low) & (df['pollution_index'] <= p_high)
df_sub = df[mask]
r_b_ctrl, _ = stats.pearsonr(df_sub['benzene'], df_sub[target_col])
r_c_ctrl, _ = stats.pearsonr(df_sub['cadmium'], df_sub[target_col])
print("\n--- Task 7: Controlled Correlations ---")
print(f"Benzene vs Malignancy (Controlled): r = {r_b_ctrl:.4f}")
print(f"Cadmium vs Malignancy (Controlled): r = {r_c_ctrl:.4f}")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
x = np.arange(2)
w = 0.35
ax1.bar(x - w/2, [r_b_naive, r_c_naive], w, label='Naive', color='indianred')
ax1.bar(x + w/2, [r_b_ctrl, r_c_ctrl], w, label='Controlled', color='steelblue')
ax1.set_xticks(x)
ax1.set_xticklabels(['Benzene', 'Cadmium'])
ax1.set_ylabel('Pearson r')
ax1.set_title('Correlation Before and After Control')
ax1.legend()
ax1.grid(axis='y', alpha=0.3)
ax2.scatter(df_sub['cadmium'], df_sub[target_col], alpha=0.5, color='forestgreen')
ax2.set_xlabel('Cadmium')
ax2.set_ylabel('Malignancy Score')
ax2.set_title('Cadmium vs Malignancy (Controlled)')
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chemical_causation.png')
print("\nSaved chemical_causation.png")