import pandas as pd
  ######Open JSON file########
#data=pd.read_json('file.json')
#print(data.to_string())

  #####Analyzing Data#########
#data=pd.read_csv('data.csv')
#ana_data=pd.DataFrame(data)
#print(ana_data.head()) #It will print first five rows from head
#print(ana_data.head(10)) # it will print 10 rows from head
#print(ana_data.tail()) #It will print first five rows from bottom
#print(ana_data.tail(10)) # it will print 10 rows from bottom

#################  Info ########################
#print(ana_data.info())

################Delete Null valued rows##################
#ana_data.dropna(inplace=True) #it will delete the complete row contains a Null value in the original
#print(ana_data.info())

###############Replace the Null value#################
#ana_data.fillna('Value',inplace=True) #it will replace all coloumns null values with "Value"
#print(ana_data.to_string())
#mean=ana_data['Calories'].mean() #it will return mean of calories coloumn
#median=ana_data['Calories'].median() #it will return median of calories coloumn
#mode=ana_data['Calories'].mode()[0]   #it will return only one mode of calories coloumn
#ana_data['Calories'].fillna(mean,inplace=True) #it will replace Calories coloumn null values with Mean
#print(ana_data.to_string())
#print('Mean = ',mean)
#ana_data['Calories'].fillna(median,inplace=True) #it will replace Calories coloumn null values with Median
#print(ana_data.to_string())
#print('Median = ',median)
#ana_data['Calories'].fillna(mode,inplace=True) #it will replace Calories coloumn null values with Mode
#print(ana_data.to_string())
#print('Mode = ',mode)

###Correct the format####
data=pd.read_csv('dirtydata.csv')
#data['Date']=pd.to_datetime(data['Date'])
#data.dropna(subset=['Date'],inplace=True)
#print(data.to_string())


