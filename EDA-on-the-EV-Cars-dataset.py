"""
EDA(Exploratory Data Analysis)On EV Cars Dataset
Steps:
1.Reading Dataset
2.Feature engineering & extracting features
3.Statistics Summary
4.Univariate Analysis
5.Bivariate Analysis
6.Multivariate Analysis

"""

"""
Install Bellow python libraries
#1.py -m pip install pandas
#2.py -m pip install numpy
#3.py -m pip install matplotlib
#4 py -m pip install seaborn

"""


# 1.Reading Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('EV_cars.csv')
print(data.head())
a, b = data.shape
print("\n\nData shape:{} * {} ".format(a, b))
print("\n\nData Information: \n")
data.info()

# rename column name 'acceleration..0.100.' to 'Acceleration'
data.rename(columns={'acceleration..0.100.': 'Acceleration'}, inplace=True)

# drop null values
data.nunique()
data.isnull().sum()
data = data.dropna()

# 2.Feature engineering & extracting features
data['Brand'] = data.Car_name.str.split().str.get(0)
data['Car'] = data['Car_name'].str.split().str[1:].apply(' '.join)
data['Car'].head()
print("\nEV Brands: ", data.Brand.unique())

# 3.Statistics Summary

print("\n\nDescriptive statistics of the numerical columns: \n", data.describe())
categorical_columns = data.select_dtypes(include=['object']).columns
numerical_columns = data.select_dtypes(include=np.number).columns

print("\ncategorical columns: ", list(categorical_columns))
print("numerical columns: ", list(numerical_columns))

# 4.Univariate Analysis
"""
Univariate Analysis: Analyzing/visualizing the dataset by taking one variable at a time
"""
for col in numerical_columns:
    skew = round(data[col].skew(), 2)
    fig = plt.figure(figsize=(15, 4))
    fig.suptitle("Histogram and BoxPlot (Skew: {})".format(skew))
    plt.subplot(1, 2, 1)
    data[col].hist(grid=False)
    plt.ylabel('count')
    plt.xlabel('{}'.format(col))
    plt.subplot(1, 2, 2)
    sns.boxplot(x=data[col])
    plt.show()

# CountPlot
fig = plt.figure(figsize=(10, 8))
plt.title('Number of EV Cars by Brand')
sns.countplot(y="Brand", data=data)
plt.show()
"""
from the above count plot we come to know Mercedes is most seen brand
"""

# Distribution Plot
plt.title('Distribution Plot')
sns.distplot(data["Price.DE."], axlabel="Price.DE.")
plt.show()

"""
Observation from Distribution plot (histogram)
Price: Right-Skewed Distribution, most of the cars in the dataset have lower prices, and there are few cars with significantly higher prices.
"""

# 5.Bivariate Analysis
"""
Bivariate Analysis: helps to understand how variables are related to each other
A Pair plot has been used to show the relationship between two Categorical variables.
"""

# plt.figure(figsize=(8, 8))
# plt.title('Pair Plot')
sns.pairplot(data[['Battery', 'Efficiency', 'Fast_charge',
             'Price.DE.', 'Range', 'Top_speed', 'Acceleration']], height=2)
# plt.show()

"""
Observations From PairPlot:
Battery is positively correlated with all other variables (more battery, higher price).
The variable "Price" has a positive correlation with "Range," "Battery," and "Top_speed."
Price increases as "Fast_charge" and "Range" increase.
"Price" is right-skewed—most cars in the dataset have lower prices, with few having significantly higher prices.
As fast-charging capability increases, efficiency decreases.
"Acceleration" is negatively correlated.

"""

"""
Bar plot shows relationship between Brand and Price
"""
top_brands = data.groupby('Brand')['Price.DE.'].mean(
).sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x=top_brands.values, y=top_brands.index, palette="viridis")
plt.title("Top 10 Brands Price in Germany", fontsize=18)
plt.xlabel("Mean Price in Germany", fontsize=14)
plt.ylabel("Brand", fontsize=14)
plt.show()

top_brands = data.groupby('Brand')['Battery'].mean(
).sort_values(ascending=False).head(20)
plt.figure(figsize=(12, 8))
sns.barplot(x=top_brands.values, y=top_brands.index, palette="viridis")
plt.title("Top 20 Brands with their Battery capacity in Germany", fontsize=18)
plt.xlabel("Battery", fontsize=14)
plt.ylabel("Brand", fontsize=14)
# plt.show()

"""Observations from BarPlot:
The most expensive EV car belongs to the Lucid brand.
The maximum capacity of the vehicle's battery in kilowatt-hours (kWh) is found in EV cars of brands such as Lotus, Lucid, VinFast, Fisker, etc.
"""

# 6.Multivariate Analysis

"""Multivariate Analysis- relationship between more than two variables.
A heat map is used for Multivariate Analysis
"""
# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()

"""Observations from Heat Map:
Heat Map gives the correlation between the variables, whether it has a positive or negative correlation.
The Range has a strong positive correlation to Battery 0.88
Price has a positive correlation to Top_spedd 0.76 as well Battery 0.70
Battery has a strong positive correlation to Range 0.88
Acceleration has negative correlation with all except efficiency
Efficiency has correlated to Top_speed, Range, and Fast_charge negatively
Top_speed has a positive correlation to Range 0.76, Fast_charge 0.79 as well Price 0.76
price,Fast_charge,Top_speed & Range all are positively correlated
"""

# Some extra Observations:
# Distribution of Top 20 Cars with Maximum Range

top_20_cars = data.head(20)
plt.figure(figsize=(10, 10))
sns.set_palette("pastel")
plt.pie(top_20_cars['Range'], labels=top_20_cars['Car_name'],
        autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Cars Based on Range (Top 20)')
plt.show()

"""
Observations from Pie Plot
From the above pie chart 'Lucid Air Dream Edition R' has the maximum Range
"""
# Top 10 Tesla Cars - Fast Charge Capability
tesla_cars = data[data['Brand'] == 'Tesla']
top_10_tesla_cars = tesla_cars.nlargest(10, 'Fast_charge')
plt.figure(figsize=(12, 8))
sns.barplot(x='Fast_charge', y='Car',
            data=top_10_tesla_cars, palette='viridis')
plt.xlabel('Fast Charge Capacity (minutes)')
plt.ylabel('Tesla EV Cars')
plt.title('Top 10 Tesla Cars - Fast Charge Capability')
plt.show()


# Top 10 Tesla Cars with Fast charging capacity
sns.scatterplot(data=data, x="Price.DE.", y="Range")
plt.title('Scatter Plot')
plt.show()


"""
Observations from Scatter Plot
As the driving range of the vehicle on a single charge in kilometers increases Price of car also increases.
"""
