# EU4 Unit Pip Summary & Visualization

This project extracts, processes, and visualizes unit pip data from Europa Universalis IV (EU4) mod files. It is designed for modders and players who want to analyze how unit stats ("pips") evolve with military technology over time, for both infantry and cavalry.

## Features
- **Data Extraction:** Parses all unit files and technology unlocks to build a comprehensive CSV of unit pip values, tech levels, and unlock years.
- **Data Merging:** Merges unit stats with their corresponding tech unlocks and years.
- **Visualization:** Plots the progression of total pips for each unit type over time, with interactive legends for easy comparison.
- **Interactivity:** Clickable legend allows you to highlight and compare specific unit types in the plot.

## Project Structure
```
Eu4UnitPipSummary/
├── plot_unit_pip.py           # Main script for plotting and interactivity
├── unit_pip_summary.py        # Script for extracting and merging unit/tech data
├── unit_pip_summary.csv       # Output data file (unit stats, tech, year, etc.)
├── technologies/
│   └── mil.txt                # Source for tech unlocks
├── units/                     # All unit .txt files
└── ...
```

## Requirements
- Python 3.8+
- matplotlib
- pandas
- seaborn

For interactive plots, you must use a GUI backend (e.g., TkAgg). This is set automatically in the script.

## Usage
1. **Extract and Merge Data:**
   - Run `unit_pip_summary.py` to generate `unit_pip_summary.csv` from your EU4 mod files.
2. **Plot and Explore:**
   - Run `plot_unit_pip.py` in a terminal (not in Jupyter or VS Code interactive window) to view interactive plots.
   - Click on a unit type in the legend to highlight its progression.

## Notes
- The y-axis grid and ticks are set to integer values, as pip values are always whole numbers.
- Only one unit type can be highlighted at a time for clarity.
- Interactive figures cannot be saved as interactive HTML; use Plotly if you need portable interactive plots.

## Example Output
- `infantry` and `cavalry` pip progression step plots, with interactive highlighting.

## License
MIT License

## Credits
- Inspired by the EU4 modding community and the need for better unit stat analysis tools.
