## Project Overview
This project performs Exploratory Data Analysis (EDA) on an EV cars dataset to understand trends, patterns, and insights using Python.

## Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Key Insights
The following insights were derived through Exploratory Data Analysis (EDA) on EV cars dataset using Python libraries: Pandas, NumPy, Matplotlib, and Seaborn.
1. Brand Analysis
Mercedes is the most common EV brand in the dataset.
Lucid produces the most expensive EV cars.
Brands like Lotus, Lucid, VinFast, and Fisker have the highest battery capacities.

2. Price Analysis
EV prices in Germany are right-skewed: most cars have lower prices, while a few are significantly expensive.
Price is positively correlated with Battery, Range, Top_speed, and Fast_charge.
Higher driving range and fast-charging capability generally mean higher prices.

3. Battery & Range
Battery capacity is strongly correlated with Range (0.88).
Top 20 EVs with the highest range show Lucid Air Dream Edition R as the leader.

4. Performance Metrics
Acceleration is negatively correlated with most variables (faster cars tend to have lower battery efficiency).
Efficiency decreases slightly as Fast_charge increases.
Top_speed has a positive correlation with Range (0.76) and Price (0.76).

5. Visual Insights
Univariate Analysis: Most cars have lower prices and moderate battery capacities.
Bivariate Analysis: Pair plots show Battery, Price, and Range are strongly interrelated.
Multivariate Analysis (Heatmap): Strong correlations observed between Price, Battery, Range, and Top_speed.
Scatter and Pie Charts: Higher-range cars tend to be more expensive.Top Tesla cars have impressive fast-charge capabilities.
