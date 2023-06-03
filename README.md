# Electricity-Power-Production-Project
#### Importing required libraries
```python
# Importing the necessary libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```
- Reading the data
- Checking for columns and it's data types,shape of data,null values
- Finding the duplicated values and unique values in each column
- Dropping the Null values
### Data Cleaning
- In data we have mixed data types extracting the data by using regular expression
- save it as string
- Droping the unnessaru features
### Data Transforamation
- Transforming the data type of columns into standard type
- Checking for correlation
### Model Building
- Splitting the data into train and test data
- converting the different scale of data into standard form by applying standard scalar
- Building the model by applying different regressin algorithems
- Select the best model which have best R2 score near to 1
- Saving the model
