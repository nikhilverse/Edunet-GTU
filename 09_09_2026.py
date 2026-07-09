import pandas as pd

# Load the dataset
df = pd.read_csv("co2_emissions_kt_by_country.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Dataset dimensions
print("\nShape of Dataset:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

#OUTPUT
'''First 5 Rows:
  country_code country_name  year      value
0          ABW        Aruba  1960  11092.675
1          ABW        Aruba  1961  11576.719
2          ABW        Aruba  1962  12713.489
3          ABW        Aruba  1963  12178.107
4          ABW        Aruba  1964  11840.743

Dataset Information:
<class 'pandas.DataFrame'>
RangeIndex: 13953 entries, 0 to 13952
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   country_code  13953 non-null  str    
 1   country_name  13953 non-null  str    
 2   year          13953 non-null  int64  
 3   value         13953 non-null  float64
dtypes: float64(1), int64(1), str(2)
memory usage: 436.2 KB
None

Shape of Dataset:
(13953, 4)

Columns:
Index(['country_code', 'country_name', 'year', 'value'], dtype='str')

Statistical Summary:
               year         value
count  13953.000000  1.395300e+04
mean    1990.732316  8.254983e+05
std       17.187585  2.788923e+06
min     1960.000000 -8.067400e+01
25%     1976.000000  1.100000e+03
50%     1992.000000  1.390000e+04
75%     2006.000000  1.642779e+05
max     2019.000000  3.434401e+07'''

# ============================================================
# GENERALIZATIONS AND ANALYSIS OF THE DATASET
# ============================================================

# Dataset Name:
# CO2 Emissions (kilotons) by Country

# Total Records (Rows): 13,953
# Total Features (Columns): 4

# Columns:
# 1. country_code
# 2. country_name
# 3. year
# 4. value

# Data Types:
# - country_code : Object (Categorical)
# - country_name : Object (Categorical)
# - year         : Integer
# - value        : Float

# ============================================================
# OVERALL OBSERVATIONS
# ============================================================

# 1. The dataset contains historical CO2 emission records for countries
#    across multiple years.

# 2. Each row represents the CO2 emission of one country in one specific year.

# 3. The dataset spans from the year 1960 to 2019,
#    giving 60 years of historical environmental data.

# 4. There are 255 unique country codes and 256 unique country names.
#    This indicates that the dataset contains both countries and regional groups
#    (for example, Africa Eastern and Southern).

# 5. The CO2 emission values are measured in kilotons (kt).

# 6. CO2 emissions vary greatly between countries.
#    The minimum value is approximately -80.67 kt,
#    while the maximum exceeds 34 million kt,
#    indicating a very wide range of emissions.

# 7. The median emission value (~13,900 kt) is much smaller than the mean
#    (~825,498 kt), showing that the dataset is highly right-skewed.
#    A few countries produce extremely high emissions compared to most countries.

# 8. The dataset contains no missing (null) values.

# 9. Since there are no null values, no data cleaning is required
#    for missing data.

# 10. This dataset is suitable for:
#     - Trend analysis
#     - Country comparison
#     - Sustainability studies
#     - Climate change analysis
#     - Time-series analysis
#     - Data visualization
#     - Machine learning after feature engineering

# ============================================================
# RELATIONSHIP BETWEEN FEATURES
# ============================================================

# country_code
# -> Unique three-letter identifier for each country or region.
# -> Used together with country_name.

# country_name
# -> Descriptive name of the country or region.
# -> Multiple records exist because each country appears for different years.

# year
# -> Represents the year when CO2 emissions were recorded.
# -> Combined with country_name, it uniquely identifies a yearly observation.

# value
# -> CO2 emissions in kilotons.
# -> This is the target variable for most analyses.
# -> Changes according to both country and year.

# Feature Relationships:
#
# country_code ------\
#                     ---> identify a country
# country_name ------/
#
# country + year -----> determines one observation
#
# country + year -----> corresponding CO2 emission value
#
# Therefore:
# value depends on both the country and the year.

# =====================================================
# CHECKING FOR NULL VALUES
# =====================================================

print("Missing Values in Each Column:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# =====================================================
# OBSERVATION
# =====================================================

# After checking the dataset, no missing (null) values were found.
# Therefore, no data was removed or modified.
# However, appropriate fillna() methods have been included to
# demonstrate how missing values would be handled if they were present.
#
# - Numerical values ('value' and 'year') would be replaced with the median.
# - Categorical values ('country_code' and 'country_name') would be replaced with the mode.
#
# This approach preserves the dataset while ensuring it is ready for analysis.