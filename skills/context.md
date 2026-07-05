# Data Cleaning Activity

## Dataset Information

- This activity uses the Air Quality Data dataset from the UCI Machine Learning Repository.
- The dataset contains hourly measurements from gas sensors deployed in an Italian city, including pollutants and environmental variables such as CO, NOx, $NO_{2}$, benzene, temperature, relative humidity, and absolute humidity.
- Missing values in this dataset are encoded using the value -200.
- Source: [https://archive.ics.uci.edu/dataset/360/air%2Bquality](https://archive.ics.uci.edu/dataset/360/air%2Bquality).

## Objective

Apply data cleaning techniques to a real air quality dataset by identifying structural problems, treating missing values, comparing imputation strategies, analyzing distributional changes, detecting outliers, and producing a cleaned dataset ready for later analysis.

## General Instructions

- Work in Python using Pandas, NumPy, Matplotlib or Seaborn, and Scikit-learn.
- Do not train a machine learning model in this activity.
- The focus is data preparation, not prediction.
- Every cleaning decision must be justified using evidence such as missing-value percentages, summary statistics, histograms, density plots, or boxplots.

---



## 1. Dataset Loading and Initial Diagnosis (15 pts)

Load the dataset into a Pandas DataFrame. Consider that the original file may require specific reading parameters such as a semicolon separator and comma decimal notation.

### Tasks

- a) Load the dataset into a DataFrame.
- b) Display the first rows of the dataset.
- c) Report the number of rows and columns.
- d) Inspect the data types of all variables.
- e) Identify empty, duplicated, or unnecessary columns.
- f) Convert date and time variables into an appropriate datetime format when possible.



### Guiding Questions

1. What structural problems do you observe in the original dataset?
2. Which variables require conversion before analysis?

---



## 2. Missing Value Identification and Basic Imputation (20 pts)

In this dataset, missing values are not originally represented as NaN; they are encoded as -200. Replace every occurrence of -200 with NaN before calculating missing-value statistics.

### Required Formulas

For each variable $X_{j}$, compute the percentage of missing values as:
$$Missing~~Percentage(X_{j})=\frac{Number~~of~~missing~~values~~in~~X_{j}}{Total~~number~~of~rows}\times100.$$

If mean imputation is used for a numerical variable X, replace a missing value with:
$$\hat{x}*{i}=\overline{x}=\frac{1}{n}\sum*{i=1}^{n}x_{i}.$$

If median imputation is used, replace a missing value with:
$$\hat{x}_{i}=median(X).$$

### Tasks

- a) Replace -200 values with NaN.
- b) Calculate the number and percentage of missing values per column.
- c) Decide whether each column should be kept, removed, or imputed.
- d) Apply at least two basic missing-value strategies:
  - Removal of rows or columns with excessive missingness.
  - Mean or median imputation for selected numerical variables.
- e) Justify each decision with a clear criterion.



### Guiding Questions

1. What threshold did you use to decide whether a column had excessive missingness?
2. Why is the median sometimes preferable to the mean when imputing numerical variables?

---



## 3. KNN Imputation and Distribution Comparison (25 pts)

Apply `KNNImputer` from Scikit-learn to impute missing numerical values. Before using KNN imputation, select only numerical variables and consider scaling them if their units are very different.

### Required Formulas

KNN imputation estimates a missing value using the values from the k most similar observations. A general weighted version is:
$$\hat{x}*{ij}=\frac{\sum*{r\in N_{k}(i)}w_{ir}x_{rj}}{\sum_{r\in N_{k}(i)}w_{ir}},$$
where $N_{k}(i)$ is the set of the k nearest neighbors of observation i, and $w_{ir}$ is the weight assigned to neighbor r.

A common distance for incomplete numerical data is computed only over the variables observed in both records. If J is the set of shared observed variables and p is the total number of variables, one possible scaled Euclidean distance is:
$$d(x,y)=\sqrt{\frac{p}{|J|}\sum_{j\in J}(x_{j}-y_{j})^{2}}.$$

### Tasks

- a) Select the numerical columns to be imputed using `KNNImputer`.
- b) Apply KNN imputation with at least two different values of k.
- c) Compare KNN imputation with mean or median imputation.
- d) For at least three variables, compare the distributions before and after imputation using histograms, density plots, or side-by-side boxplots.
- e) Compare summary statistics before and after imputation: mean, median, standard deviation, minimum, maximum, and IQR.



### Guiding Questions

1. Which imputation method preserves the original distribution more clearly?
2. Did KNN imputation change the variability or shape of the selected variables?
3. What value of k produced the most reasonable results? Justify your answer.

---



## 4. Outlier Detection with Tukey's Rule and Z-score (25 pts)

Select at least three relevant numerical variables, such as CO (GT), C6H6 (GT), NOx(GT), NO2(GT), T, RH, or AH. Detect outliers using both Tukey's rule and the Z-score method.

### Required Formulas

The interquartile range is:
$$IQR=Q_{3}-Q_{1}.$$

Tukey's lower and upper thresholds are:
$$Lower~~Bound=Q_{1}-1.5\times IQR,$$
$$Upper~~Bound=Q_{3}+1.5\times IQR.$$

A value $x_{i}$ is considered an outlier under Tukey's rule if:
$$x_{i}<Q_{1}-1.5\times IQR \text{ or } x_{i}>Q_{3}+1.5\times IQR$$

The Z-score of an observation is:
where $\mu$ is the mean and $\sigma$ is the standard deviation. A common rule is:
$$Z_{i} > 3.$$

### Tasks

- a) Generate boxplots for the selected variables.
- b) Detect outliers using Tukey's rule.
- c) Detect outliers using the Z-score method.
- d) Create a table showing the number and percentage of outliers detected by each method.
- e) Compare the results of both methods.



### Guiding Questions

1. Do Tukey's rule and Z-score detect the same observations as outliers?
2. Are the extreme values likely to be measurement errors, sensor behavior, or real pollution events?
3. Which method is more appropriate for skewed variables? Explain your reasoning.

---



## 5. Outlier Treatment and Final Clean Dataset (15 pts)

Apply one treatment strategy for the detected outliers. The selected strategy must be justified according to the behavior of each variable.

### Required Formula

If winsorization or clipping is applied using lower and upper limits L and U, each value can be transformed as:
$$x_{i}^{*}=min(max(x_{i},L),U).$$

For Tukey-based clipping, use:
$$L=Q_{1}-1.5\times IQR$$
$$U=Q_{3}+1.5\times IQR.$$

### Tasks

- a) Apply an outlier treatment technique, such as winsorization, clipping using Tukey thresholds, or justified conservation of extreme values.
- b) Generate boxplots after the treatment.
- c) Compare the dataset before and after cleaning using the table below.
- d) Save the cleaned dataset as `air_quality_clean.csv`.



### Comparison Table


| Element                               | Before Cleaning | After Cleaning |
| ------------------------------------- | --------------- | -------------- |
| Number of rows                        |                 |                |
| Number of columns                     |                 |                |
| Total missing values                  |                 |                |
| Columns removed                       |                 |                |
| Variables imputed with mean or median |                 |                |
| Variables imputed with KNNImputer     |                 |                |
| Variables treated for outliers        |                 |                |




### Guiding Questions

1. What changed the most after the complete cleaning process?
2. Did the final dataset preserve the original information reasonably well?
3. What risks could appear if these cleaning steps were applied automatically without analysis?

---



## Restrictions

- Do not train any machine learning model.
- Do not remove rows or columns without justification.
- Do not replace all missing values automatically with the mean.
- Do not treat every outlier as an error without considering the context of air pollution and sensor data.
- All decisions must be supported with visual or statistical evidence.



## Zero Credit Conditions

The activity will receive no credit if any of the following issues are identified:

- The notebook is not shared with reading permissions enabled.
- The submission appears to be entirely generated by artificial intelligence or demonstrates excessive AI use.
- The notebook cells are not executed before submission.

