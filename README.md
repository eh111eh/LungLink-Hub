# LungLink Hub: Global Correlations of Lung Cancer Survival Rates with Societal Factors

## Abstract / Summary
This study explores the correlation between lung cancer survival rates and societal factors on a global scale. While existing research has linked lung cancer to environmental pollutants and resource accessiblity in the U.S., little is known about how broader societal influences contribute to varied health outcomes worldwide. Through a comprehensive analysis of diverse variables, including healthcare accessibility, socio-economic conditions, and cultural factors, this research aims to uncover patterns and relationships that can deepen our understanding of lung cancer survival dynamics.

By investigating the interplay between lung cancer outcomes and societal factors, this research seeks to inform public health policies and resource allocation strategies. The study's findings may offer valuable insights into addressing the complexities of lung cancer on a global level, ultimately contributing to more effective interventions and equitable health outcomes.

## Selected Theme
HealthCare - Health Equity

## Goal / Purpose

**Value for end-user**: <br/>
This research aims to provide valuable insights for policymakers, healthcare professionals, and public health organizations. By understanding the complex interplay between societal factors and lung cancer outcomes, it contributes to the development of more effective interventions and strategies for improving global health equity.

**Input, output, type of problems**
  - Input: Seven key factors including healthcare accessibility, socio-economic conditions, and cultural influences.
  - Output: Lung cancer survival rates by country and year.
  - Type of Problems: Exploratory data analysis, correlation analysis, regression analysis.

## Tool
Python, Flask, SQL(MySQ)L, HTML/CSS/JavaScript

## Data

**Source**: <br/>
The data is sourced from the WorldBank site and covers multiple countries globally.

**Quantity, shape, type**: <br/>
The dataset consists of multiple dataframes. The primary dataframe, denoted as X, contains information for different countries and years. The observations (rows) are indexed by the 'country' and further contextualized by the 'year' attribute, with columns representing various features such as poverty proportion, forest area, health expenditure, etc. There is also a dataframe denoted as y_mortality containing data on the age-standardized rate of mortality for lung cancer.

**Input features**: <br/>
The input features in the X dataframe include:

- c_dollar2_poverty: Proportion of Population Pushed Below 3 dollar and 65 cents Poverty Line by Out-of-Pocket Health Care Expenditure
- c_forest_area: The Percentage of Land Area covered by Forest
- c_health_expenditure: The Percentage of a Country's GDP that goes towards Health Expenditures
- c_out_of_pocket: Out-of-Pocket Expenditure per Capita (Current US Dollars)
- c_physician: Physicians (Per 1000 People)
- c_tuberculosis: Incidence of Tuberculosis (Per 100,000 People)
- c_urban_pop: The Percentage of the Total Population living in Urban Areas

## Model
**Model in Use**: <br/> 
Linear Regression, Adaboost, GBRT, Random Forest, Stacking, Decision Tree, LSTM (Neural Network)

**How to evaluate performance**: <br/>
The performance of the research can be evaluated through the following metrics:

- Correlation coefficients between societal factors and lung cancer survival rates.
- Mean Squared Error (MSE) for regression models predicting lung cancer survival rates.
- F1 Score for classification models assessing the impact of societal factors on survival outcomes.

## Usage
**URL**: <br/>
https://lunglink-hub.onrender.com

**Installation Instructions**

**Prerequisites**

**Usage Guidelines**

## Reference
- Lung Cancer Survival Rates : https://gco.iarc.fr/overtime/en/dataviz/trends
- Proportion of Population Pushed Below 3.65 Poverty Line by Out-of-Pocket Health Care Expenditure : https://data.worldbank.org/indicator/SH.UHC.NOP2.ZS
- Forest Area Coverage : https://data.worldbank.org/indicator/AG.LND.FRST.ZS
- Current Health Expenditure (% of GDP) : https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS
- Domestic General Government Health Expenditure per Capita (Current US Dollars) : https://data.worldbank.org/indicator/SH.XPD.GHED.PC.CD
- Out-of-Pocket Expenditure per Capita (Current US Dollars) : https://data.worldbank.org/indicator/SH.XPD.OOPC.PC.CD
- Physicians (Per 1000 People) : https://data.worldbank.org/indicator/SH.MED.PHYS.ZS
- Incidence of Tuberculosis (Per 100,000 People) : https://data.worldbank.org/indicator/SH.TBS.INCD
- Urban Population (% of Total Population) : https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS"

# Collaborators
- Hwayeon Kang
- Minha Kim
