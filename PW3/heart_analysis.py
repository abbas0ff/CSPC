import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# 1. Load data
df = pd.read_csv('heart.csv')
print("Shape:", df.shape)
print("\nFirst rows:")
print(df.head())
cols = ['age', 'chol', 'trestbps', 'thalach']
print("\nStats:")
print(df[cols].describe())
# 2. Xistograms
fig, axes = plt.subplots(2, 2, figsize=(9, 7))
axes = axes.flatten()
for i, col in enumerate(cols):
    axes[i].hist(df[col], bins=15, color='skyblue', edgecolor='black')
    axes[i].set_title(f'Distribution: {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')
    axes[i].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('heart_distributions.png')
# 3. Normality testss (Shapiro-Wilk)
print("\n--- Normality Tests ---")
for col in cols:
    stat, p = stats.shapiro(df[col])
    res = "Normal" if p > 0.05 else "Not Normal"
    print(f"{col:10s} | p = {p:.4e} -> {res}")
# 4. Compare thalach (Healthy vs Disease)
healthy = df[df['target'] == 0]['thalach']
disease = df[df['target'] == 1]['thalach']
t_stat, p_val = stats.ttest_ind(healthy, disease)
print("\n--- Heart Rate Comparison ---")
print(f"Healthy mean: {healthy.mean():.2f} +/- {healthy.sem():.2f}")
print(f"Disease mean: {disease.mean():.2f} +/- {disease.sem():.2f}")
print(f"p-value: {p_val:.4e}")
# Plot means with SEM error bars
plt.figure(figsize=(5, 4))
means = [healthy.mean(), disease.mean()]
sems = [healthy.sem(), disease.sem()]
labels = ['Healthy', 'Disease']
plt.bar(labels, means, yerr=sems, capsize=4, color=['green', 'red'], alpha=0.7)
plt.ylabel('Max Heart Rate')
plt.title('Heart Rate by Disease Status')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('thalach_by_target.png')
# 5. Correlation (age vs thalach)
r_p, p_p = stats.pearsonr(df['age'], df['thalach'])
print(f"\nPearson r (age vs thalach): {r_p:.4f} (p = {p_p:.4e})")
plt.figure(figsize=(6, 4))
plt.scatter(df['age'], df['thalach'], alpha=0.5, color='purple')
m, b = np.polyfit(df['age'], df['thalach'], 1)
plt.plot(df['age'], m * df['age'] + b, color='red', linestyle='--')
plt.xlabel('Age')
plt.ylabel('Max Heart Rate')
plt.title('Age vs Max Heart Rate')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('age_vs_thalach.png')
# Bonus: Unpredictability (Entropy)
p = df['target'].value_counts(normalize=True)
entropy = -np.sum(p * np.log2(p))
print(f"\nTarget Entropy: {entropy:.4f} bits")