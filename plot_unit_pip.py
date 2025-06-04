import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('unit_pip_summary.csv')

# Remove rows with missing or non-numeric year or total_pips
df = df[pd.to_numeric(df['year'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['total_pips'], errors='coerce').notnull()]
df['year'] = df['year'].astype(float)
df['total_pips'] = df['total_pips'].astype(float)

# Remove rows with missing unit_type
df = df[df['unit_type'].notnull()]

# Sort by year for each unit_type
df = df.sort_values(['unit_type', 'year'])

sns.set(style="whitegrid")

# Infantry plot as step function
plt.figure(figsize=(14, 8))
infantry_df = df[df['type'] == 'infantry']
for unit_type, group in infantry_df.groupby('unit_type'):
    years = list(group['year'])
    pips = list(group['total_pips'])
    if len(years) > 0 and years[-1] < 1812:
        years.append(1812)
        pips.append(pips[-1])
    plt.step(years, pips, where='post', label=unit_type)
plt.xlabel('Year')
plt.ylabel('Total Pips')
plt.title('EU4 Infantry Total Pips Progression by Unit Type (Step)')
plt.xlim(left=infantry_df['year'].min(), right=1812)
plt.legend(title='Unit Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('infantry.png', dpi=300)
plt.show()

# Cavalry plot as step function
plt.figure(figsize=(14, 8))
cavalry_df = df[df['type'] == 'cavalry']
for unit_type, group in cavalry_df.groupby('unit_type'):
    years = list(group['year'])
    pips = list(group['total_pips'])
    if len(years) > 0 and years[-1] < 1812:
        years.append(1812)
        pips.append(pips[-1])
    plt.step(years, pips, where='post', label=unit_type)
plt.xlabel('Year')
plt.ylabel('Total Pips')
plt.title('EU4 Cavalry Total Pips Progression by Unit Type (Step)')
plt.xlim(left=cavalry_df['year'].min(), right=1812)
plt.legend(title='Unit Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('cavalry.png', dpi=300)
plt.show()
