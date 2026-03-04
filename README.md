# TLC-Taxi-Fare-Estimation-App
This app is developed to enable TLC riders to estimate the taxi fares in advance of their ride. 
<br>
<br>

While understanding this data, I came across two important features, 'Total amount' and 'Distance travelled' and found that larger distance doesn't necessarily imply maximum fare.
<br>
# Exploratory Data Analysis
Applied EDA and Data Visualization to see how a general taxi ridership looks like. This includes data structuring and cleaning, matplotlib/seaborn visualizations and a box plot of the ride durations and time series plots which are plotted to help understand the data.
<br>
<br>
While analysing the data, there were several trips that have a trip distance of "0.0." What might those trips be? Will they impact our model? These were the questions I came across. In this scenerio, Boxplot, Bar chart and Scatter plot was the most useful.
<br>
Box plot was used to determine outliers and to find where the bulk of the data points reside in terms of trip_distance, total_amount and tip_amount.
Histogram to visualize the trends and patterns and outliers of critical variables, such as DOLocationID, tip_amount, trip_distance and total_amount. And a Bar chart to determine average number of trips per month and weekday, etc.
<br>
Result : 
<br>
* The distribution for tip amount is right-skewed, with nearly all the tips in the $0-3 range.
* The total cost of each trip also has a distribution that skews right, with most costs falling in the $5-15 range.
* Mean tip amount varies very little by passenger count. Although it does drop noticeably for four-passenger rides, it's expected that there would be a higher degree of fluctuation because rides with four passengers were the least plentiful in the dataset (aside from rides with zero passengers).
* Monthly rides are fairly consistent, with notable dips in the summer months of July, August, and September, and also in February.
* Wednesday through Saturday had the highest number of daily rides, while Sunday and Monday had the least.
* Thursday had the highest gross revenue of all days, and Sunday and Monday had the least. Interestingly, although Saturday had only 35 fewer rides than Thursday, its gross revenue was ~$6,000 less than Thursday's — more than a 10% drop.
* Monthly revenue generally follows the pattern of monthly rides, with noticeable dips in the summer months of July, August, and September, and also one in February.
* A bar plot of mean trip distances by drop-off location by distance was created. It indicates that the drop-off points are relatively evenly distributed over the terrain. To note: no geographic coordinates were included in this dataset, so there was no obvious way to test for the distibution of locations.
<br>
Although geographic coordinates were unavailable, the cumulative distribution curve resembles a normal distribution, suggesting that drop-off locations are relatively evenly dispersed rather than heavily concentrated.
