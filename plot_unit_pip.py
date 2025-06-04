import matplotlib
matplotlib.use('TkAgg')  # Ensure interactive backend
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

# --- Helper for interactive legend using legend pick events ---
def make_legend_interactive(ax, lines, labels):
    leg = ax.legend(title='Unit Type', bbox_to_anchor=(1.05, 1), loc='upper left', fancybox=True, shadow=True)
    lined = dict()
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(5)  # 5 pts tolerance
        lined[legline] = origline
    # Make legend text also clickable
    for legtext, origline in zip(leg.get_texts(), lines):
        legtext.set_picker(True)
        lined[legtext] = origline
    highlight_width = 8  # Increased from 4
    normal_width = 2
    highlight_alpha = 1.0
    normal_alpha = 0.5
    highlighted = {'line': None}
    def on_pick(event):
        legitem = event.artist
        origline = lined.get(legitem)
        if origline is None:
            return
        # Unhighlight any previously highlighted line
        if highlighted['line'] is not None and highlighted['line'] is not origline:
            highlighted['line'].set_linewidth(normal_width)
            highlighted['line'].set_alpha(normal_alpha)
        # Toggle highlight for the clicked line
        lw = origline.get_linewidth()
        if lw == highlight_width:
            origline.set_linewidth(normal_width)
            origline.set_alpha(normal_alpha)
            highlighted['line'] = None
        else:
            origline.set_linewidth(highlight_width)
            origline.set_alpha(highlight_alpha)
            highlighted['line'] = origline
        ax.figure.canvas.draw()
    ax.figure.canvas.mpl_connect('pick_event', on_pick)
    # Set all lines to normal width/alpha
    for line in lines:
        line.set_linewidth(normal_width)
        line.set_alpha(normal_alpha)

# Infantry plot as step function (interactive legend)
plt.figure(figsize=(14, 8))
infantry_df = df[df['type'] == 'infantry']
ax = plt.gca()
lines = []
labels = []
for unit_type, group in infantry_df.groupby('unit_type'):
    years = list(group['year'])
    pips = list(group['total_pips'])
    if len(years) > 0 and years[-1] < 1812:
        years.append(1812)
        pips.append(pips[-1])
    line, = ax.step(years, pips, where='post', label=unit_type)
    lines.append(line)
    labels.append(unit_type)
plt.xlabel('Year')
plt.ylabel('Infantry Pips')
plt.xlim(left=infantry_df['year'].min(), right=1812)
make_legend_interactive(ax, lines, labels)
plt.tight_layout()
plt.show()

# Cavalry plot as step function (interactive legend)
plt.figure(figsize=(14, 8))
cavalry_df = df[df['type'] == 'cavalry']
ax = plt.gca()
lines = []
labels = []
for unit_type, group in cavalry_df.groupby('unit_type'):
    years = list(group['year'])
    pips = list(group['total_pips'])
    if len(years) > 0 and years[-1] < 1812:
        years.append(1812)
        pips.append(pips[-1])
    line, = ax.step(years, pips, where='post', label=unit_type)
    lines.append(line)
    labels.append(unit_type)
plt.xlabel('Year')
plt.ylabel('Cavalry Pips')
plt.xlim(left=cavalry_df['year'].min(), right=1812)
make_legend_interactive(ax, lines, labels)
plt.tight_layout()
plt.show()
