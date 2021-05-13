 #LESSON 2.10 - NUMPY MODULE | used as a complement for the shortcomings of python's list/array
import numpy as np  #we have already done this in python lessons, you must already know this
np1 = np.array([1,2,3,4])  #creating a list with numpy | you could also create 2 dimensional array
print(np1.shape)  #know the size of the list
print(np1.dtype)  #know the datatype contained in the list
np2 = np.arange(0,10,1)  #create a range() method
np3 = np.linspace(0,10,20)  #create random list that has 20 parts
np4 = np.random.rand(5,5)  #since we input 2 arguments that means we would be creating 2 dimensional list, the contents are random and can be accessed like normal list
np5 = np.random.randn(3,3)  #same as above but this is negative

#LESSON 2.11 - PANDAS MODULE | used for reading csv
import pandas as pd
#data1 = pd.read_csv("C:/Users/CMRDrug2004/Users/Desktop/Renz/file.csv", header=0) #read the csv file
#data1.head(10) #this means show the 10 rows of the csv file
#data1.describe() #it analyzes the value of the column, it shows count,mean,25% percentile, etc.
#data1.iloc[0] #it shows the complete data of the one in the first column
#data1.loc["specifySomething"] #it shows the complete data that matches the keyword you specified in argument

#LESSON 2.12 - SEABORN MODULE | alt to matplotlib, this is for data visualization, plotting graphs
import seaborn as sns
#sns.distplot(data2,age) #plot in a graph the age column included in data2

#LESSON 6.31 - DATA IMPORTING AND PREPROCESSING
df = pd.read_csv("House_Price.csv", header = 0) #this is where pandas module become useful
print(df.head()) #show the first five rows of data
print(df.shape) #show how many columns

#LESSON 6.34 - RUNNING EXTENDED DATA DICTIONARY (EDD)
print(df.describe())
print(sns.jointplot(x="n_hot_rooms", y = "price", data = df)) #plot this speicific variable to visualize the data
print(sns.jointplot(x="rainfall", y="price", data = df))
print(sns.countplot(x="airport", data=df))
print(sns.countplot(x="waterbody", data = df))
#OBSERVATIONS
#n_hot_rooms and rainfall has outleirs
#n_hos_beds has missing values
#bus_ter is a useless variable since every answer is yes
#crime_rate has skewness or outliers

#LESSON 6. 37 - OUTLIER TREATMENT - capping and flooring technique was used here
#treating the outlier in n_hot_rooms
print(df.info()) #identify the datatype of the variables in the spreadsheet
uv = np.percentile(df.n_hot_rooms,[99])[0] #look at the 99th percentile of var n_hot_rooms
print(df[(df.n_hot_rooms>uv)])
df.n_hot_rooms[(df.n_hot_rooms > 3*uv)] = 3*uv #3 is a random number the instructor used

#treating the outlier in rainfall
print(np.percentile(df.rainfall,[1])[0])
lv = np.percentile(df.rainfall,[1])[0]
print(df[(df.rainfall < lv)])
df.rainfall[(df.rainfall <0.3*lv)] = 0.3*lv

print(sns.jointplot(x="crime_rate", y="price", data = df))
print(df.describe()) #print the edd, since the n_hot_rooms and rainfall's outlier has been treated, have a look now

#LESSON 6.40 - MISSING VALUE IMPUTATION
print(df.info) #here you could see how many items are blank by comparing it to other variables
df.n_hos_beds = df.n_hos_beds.fillna(df.n_hos_beds.mean()) #we are filling the blanks with mean