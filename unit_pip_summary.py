import glob
import os
import re
import pandas as pd

# Directory containing unit files
unit_dir = os.path.dirname(__file__) + "/units/"
pattern = os.path.join(unit_dir, '*.txt')  # Match all .txt files

# Pip fields to extract
pip_fields = [
    'maneuver', 'offensive_morale', 'defensive_morale',
    'offensive_fire', 'defensive_fire',
    'offensive_shock', 'defensive_shock'
]

# --- Parse mil.txt for unit unlocks ---
mil_path = os.path.join(os.path.dirname(__file__), 'mil.txt')
with open(mil_path, encoding='utf-8') as f:
    lines = f.readlines()

unit_unlocks = {}
inside_tech = False
brace_level = 0
block_lines = []
current_tl = None
current_year = None
for i, line in enumerate(lines):
    if re.match(r'\s*technology\s*=\s*{', line):
        inside_tech = True
        brace_level = 1
        block_lines = [line]
        continue
    if inside_tech:
        block_lines.append(line)
        brace_level += line.count('{') - line.count('}')
        if brace_level == 0:
            block = ''.join(block_lines)
            tl_match = re.search(r'#\s*Tech\s*(\d+)', block)
            tl = int(tl_match.group(1)) if tl_match else None
            year_match = re.search(r'year\s*=\s*(\d+)', block)
            year = int(year_match.group(1)) if year_match else None
            for enable in re.findall(r'enable\s*=\s*([\w_]+)', block):
                unit_unlocks[enable] = {'tech_level': tl, 'year': year}
            inside_tech = False
            block_lines = []

rows = []
for filepath in glob.glob(pattern):
    print(f'Processing {filepath}')
    try:
        with open(filepath, encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        try:
            with open(filepath, encoding='utf-8-sig') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            with open(filepath, encoding='latin-1') as f:
                lines = f.readlines()
    content = ''.join(lines)
    unit_name = os.path.splitext(os.path.basename(filepath))[0]
    # Match only the exact line for type and unit_type
    type_match = re.search(r'^type\s*=\s*(\w+)', content, re.MULTILINE)
    unit_type_match = re.search(r'^unit_type\s*=\s*(\w+)', content, re.MULTILINE)
    type_value = type_match.group(1) if type_match else ''
    unit_type_value = unit_type_match.group(1) if unit_type_match else ''
    # Extract pips
    pips = {}
    for field in pip_fields:
        match = re.search(rf'{field}\s*=\s*(-?\d+)', content)
        pips[field] = int(match.group(1)) if match else 0
    # Find unlock info from mil.txt
    unlock_info = unit_unlocks.get(unit_name, {'tech_level': None, 'year': None})
    row = {'unit': unit_name, 'type': type_value, 'unit_type': unit_type_value,
           'tech_level': unlock_info['tech_level'], 'year': unlock_info['year']}
    row.update(pips)
    # Exclude 'maneuver' from total_pips
    total_pips = sum(v for k, v in pips.items() if k != 'maneuver')
    row['total_pips'] = total_pips
    rows.append(row)

# Create DataFrame and save as CSV
pip_table = pd.DataFrame(rows)
pip_table.to_csv(os.path.join(os.path.dirname(__file__), 'unit_pip_summary.csv'), index=False)
print(pip_table)
