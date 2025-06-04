# EU4 Unit Pip Summary & Visualization

本项目用于从《欧陆风云4》（Europa Universalis IV, EU4）模组文件中提取、处理并可视化单位属性（pips）数据。适合希望分析不同兵种（步兵、骑兵）随军事科技进步而属性变化的模组作者和玩家。

## 功能特色
- **数据提取：** 解析所有单位文件和科技解锁，生成包含单位pips、科技等级和解锁年份的完整CSV。
- **数据合并：** 将单位属性与其对应的科技解锁和年份合并。
- **可视化：** 绘制各兵种单位pips随时间变化的阶梯图，支持交互式图例，便于对比。
- **交互性：** 图例可点击，突出显示并对比特定兵种。

## 项目结构
```
Eu4UnitPipSummary/
├── plot_unit_pip.py           # 主绘图与交互脚本
├── unit_pip_summary.py        # 单位/科技数据提取与合并脚本
├── unit_pip_summary.csv       # 输出数据文件（单位属性、科技、年份等）
├── technologies/
│   └── mil.txt                # 科技解锁数据源
├── units/                     # 所有单位 .txt 文件
└── ...
```

## 依赖环境
- Python 3.8+
- matplotlib
- pandas
- seaborn

交互式绘图需使用GUI后端（如TkAgg），脚本已自动设置。

## 使用方法
1. **数据提取与合并：**
   - 运行 `unit_pip_summary.py`，从EU4模组文件生成 `unit_pip_summary.csv`。
2. **绘图与交互探索：**
   - 在终端（不要在Jupyter或VS Code交互窗口）运行 `plot_unit_pip.py`，查看交互式图表。
   - 点击图例中的兵种名称可高亮其属性变化。

## 说明
- y轴网格与刻度仅显示整数，因为pips属性为整数。
- 为便于对比，任一时刻仅允许高亮一个兵种。
- 交互式图无法保存为可交互HTML，如需便携交互图请用Plotly等库。

## 示例输出
- 步兵与骑兵pips随时间变化的阶梯图，支持交互高亮。

## 许可证
MIT License

## 致谢
- 灵感来源于EU4模组社区及对更好单位属性分析工具的需求。

---

# English Version

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
