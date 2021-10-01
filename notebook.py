import numpy as np
import pandas as pd

### This all code is written to scale user inputs, later two variables are sent to app.py###
# 'le' and 'ss' are the two vaiables that is  below

#load the train data
train = pd.read_csv('pickel-csv-files/train.csv')

# We are dropping the columns that is not required 
train.drop(columns=['PassengerId', 'Name','Ticket','Embarked','Cabin' ], axis=1, inplace=True)

# We find nan values in the Age column which we will remove now
train = train.fillna(train.Age.mean())

#remove outliers
outliers_fare = train['Fare'].quantile(1)
train = train[train.Fare < outliers_fare]
# we removed the outliers from the Fare column
# using an arithematic and quantile built in method

# we only need the data, not the index and the column
x = train.iloc[:,1:7].values 

# In the above values you see Sex data which is in categorical format, lets convert it into integers 
# LabelEncoder can be used to normalize labels
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x[:,1] = le.fit_transform(x[:,1])

## The idea behind StandardScaler is that it will transform your data such 
## that its distribution will have a mean value 0 and standard deviation of 1 (Standard Normal Distribution)
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
x = ss.fit_transform(x)