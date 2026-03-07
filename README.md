# TLC-Taxi-Fare-Estimation-App
This project analyzes NYC TLC taxi trip data to understand ride patterns and build a system that helps riders estimate taxi fares before their trip.
<br>
## Problem Statement

Taxi riders often do not know the estimated fare before starting a trip. The goal of this project is to analyze New York City taxi trip data and explore key factors that influence taxi fares, such as trip distance, duration, passenger count, and tipping behavior.

Through exploratory data analysis (EDA), this project aims to identify patterns, detect anomalies, and understand relationships between variables. These insights will support the future development of a regression model that can estimate taxi fares before a ride.

## Dataset

The dataset contains information about taxi trips such as pickup time, drop-off time, trip distance, payment type, and fare details.
<br>
Columns in the dataset include:

- `VendorID`
- `tpep_pickup_datetime`
- `tpep_dropoff_datetime`
- `passenger_count`
- `trip_distance`
- `payment_type`
- `fare_amount`
- `tip_amount`
- `total_amount`

`payment_type` values:

| Value | Payment Method |
|------|----------------|
| 1 | Credit Card |
| 2 | Cash |
| 3 | No Charge |
| 4 | Dispute |

## Objectives
* Analyze taxi trip data to identify patterns in fare amount, trip distance, tips, and ride demand.

* Perform exploratory data analysis (EDA) to uncover trends and anomalies in the dataset.

* Build a predictive model for taxi fare estimation.

* Evaluate strategies such as A/B testing to improve prediction performance.

## Key Tasks Performed

### 1. Data Understanding and Initial Exploration

- Examined the structure and characteristics of the TLC taxi dataset to understand available features and data types.
- Used summary statistics and dataset inspection techniques to explore variables related to **trip distance, fare amount, tips, and ride patterns**.
- Performed **data structuring, sorting, and filtering** to gain a deeper understanding of the dataset before analysis.

### 2. Exploratory Data Analysis (EDA)

- Conducted exploratory analysis to identify **patterns, anomalies, and potential outliers** in the dataset.
- Used statistical summaries to examine **distributions and relationships between variables**.
- Visualized key variables using **bar charts, box plots, histograms and time-series plots ** to analyze **trip distance, fare amounts, and tip distributions** over time.

### 3. Outlier Investigation

- Investigated unusual observations such as **trips with zero distance** and analyzed their potential impact on future modeling.

  ## Key Insights

* Most taxi fares fall between $5–$15, while tips are typically $0–$3.

* Ride demand is highest Wednesday–Saturday, and lowest Sunday–Monday.

* Revenue peaks on Thursdays despite similar ride volume on Saturdays.

* Monthly demand shows dips during summer months and February.

* Trip distances appear evenly distributed across drop-off locations despite lack of geographic coordinates.
<br>

### 4. Hypothesis Testing


Before performing hypothesis testing, the average fare amount was calculated for each payment type.

Based on the averages shown, it appears that customers who pay in **credit card** tend to pay a larger fare amount than customers who pay in **cash**. However, this difference might arise from random sampling rather than being a true difference in fare amount. To assess whether the difference is statistically significant, a hypothesis test was conducted.

**Null Hypothesis (H₀):**  
The average fare amount is the same for credit card and cash payments.

**Alternative Hypothesis (H₁):**  
The average fare amount differs between credit card and cash payments.

### Significance Level

```
α = 0.05
```
### Result

```
Ttest_indResult(statistic=6.866800855655372, pvalue=6.797387473030518e-12)
```

Since the p-value is significantly smaller than the significance level of 0.05, the null hypothesis is rejected. This indicates that there is a **statistically significant difference in the average fare amount between credit card and cash payments**.

## Important Note

The analysis suggests that trips paid with credit cards have a higher average fare than those paid with cash. However, this dataset is observational and passengers were not randomly assigned a payment method. Therefore, the hypothesis test assumes random grouping for analysis. In reality, other factors (such as longer trips being more likely to be paid by credit card) may influence the results. As a result, the findings indicate a statistical difference but do not necessarily imply that payment type causes higher fares.

### 5. Next Steps (Work in Progress)

- Perform **data cleaning and preprocessing** to handle inconsistencies and outliers.
- Apply **feature engineering and predictive modeling** to build a taxi fare estimation model.



<br>

