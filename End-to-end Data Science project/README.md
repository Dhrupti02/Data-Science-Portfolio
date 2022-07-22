**Language:** Python 3

**Installation:** Flask, XGBoost

**Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, statsmodels 

**End-to-end data science projects**

An end-to-end data science project goes through a series of steps called data science life cycles.
Data science life cycle
- In a real-world scenario, a data science project goes through a series of steps or cycles.

![image](https://user-images.githubusercontent.com/56231883/178240253-8215b271-dd0c-41ee-bc6f-9e38511cd46a.png)


- Business understanding: What will you do with data without having a specific problem? The goal should be clear when doing data science for a particular business. You need to understand the client's requirements.
- Data Understanding: After understanding the business requirements, you should know in which format the data you need, such as the structure of the data, and the number of features we need.
- Data preparation: The gathered data are not always pure. It can have missing values, outliers, inaccurate data, etc. Some tools and techniques help handle them.
- EDA: Exploratory data analysis is getting insights from the data. Before performing modeling, we can find insights from the data using some visualizations. 
- Data modeling: The model takes organized data as an input and gives the output. Several models use for modeling purposes. More than one model can be used for a particular problem. Then we will select the best model.
- Model evaluation: The performance of the model can be evaluated using the performance metrics. Before choosing that one model that can be deployed, the model will be evaluated.
- Model deployment: In the end, the more accurate model will be deployed. Now whenever the new data will be applied, this model will predict the output.


### Missing values:

- In the dataset, missing values occur when no data is stored. The reasons for missing data can be, 
  •	People hesitate to fill in the information
  •	Equipment malfunction
  •	Forget to fill in the information
  
- If Missing values are not handled properly, it can lead to biased predictions. The absence of data reduces the statical power. It can directly affect the distribution of data.

- There are three types of missing data:
  **•	MAR (Missing At Random)**
  **• MCAR (Missing Completely At Random)**
  **•	MNAR (Missing Not At Random)**
  
- It is advisable to find out which type of missing data is in the dataset because there are different techniques for handling missing data for each missing data type. 
If the dataset is small and it has missing values, we should not drop the missing values. If the dataset is large enough, we can delete the missing values.

#### MCAR (Missing Completely At Random):
- We can say data are MCAR when the missingness is independent of the observed and unobserved data. Meaning, that when the data is missing, it has no relationship with other variables in the dataset.

#### MAR (Missing At Random):
- We can say data are MAR when the data are intentionally missing, and there is some relationship of missing data with other variables in the feature. 
- For example, in a depression survey, male participants are less likely to complete the survey. Missing values in this survey depend on the gender variable.

#### MNAR (Missing Not At Random):
- We can say data are MNAR when the data are intentionally missing, and missingness is related to the events or factors which are not observed by the researcher.
- Let’s take the above example, a person with severe depression will refuse to complete the survey. Now, this factor of missingness is not observed by the researcher.

#### Approaches to handle missing values
**1.	Delete the rows that have missing values**
- They common approach is to delete the rows with missing values. But it is not always or, in most cases work. Removing rows can lead to loss of information.

**2.	Replace value with mean, median, or mode.**
- We can replace missing values with mean, but the problem is if the dataset has outliers, the mean will not be appropriate. In that case, outliers need to be treated.
- We can replace it with median if there are outliers in the dataset.

**3.	Imputation**
- There are various imputation techniques to fill the missing values.

For detailed explanation about missing values you can read blogs here, 
- https://www.freecodecamp.org/news/how-to-handle-missing-data-in-a-dataset/
- https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668100/

### Outlier:
- In statistics, an outlier is a data point that is far away from the normal distribution of the data.

![image](https://user-images.githubusercontent.com/56231883/178240782-3bf8ae94-2af5-49c9-bcb6-0f9ca31086f4.png)

- In the above graph, we can consider G and N as outliers because they are not following the linear line.
 
**How to detect outliers**

  •	There are various ways to detect outliers.
  
  •	The common way is to visualize the data. Boxplot is a common approach to detect outliers. A scatterplot can also be used. 
  
  •	Another method is to use IQR (Interquartile Range). IQR divide a dataset into quartile. The data points below the low quartile range and above the upper quartile range will be considered an outlier.
  
  ![image](https://user-images.githubusercontent.com/56231883/178240855-8181f4d8-3e67-4c9a-899d-245167cb593c.png)
  
  •	Another method is z-scores. A data point whose z-score falls out of the 3rd standard deviation is an outlier.
 
**How to treat outliers**

  •	The Simple approach is to remove outliers. But sometimes outliers contain useful information. Hence, it’s not a good choice to remove outliers.
  
  •	Another approach is quantile-based flooring and capping. In this technique, the outlier is capped at a certain value above the 90th percentile value or floored at a factor below the 10th percentile value.
  
  •	Another approach is Mean/Median imputation.


