##vewing the data :one of the most used method for quick overview of dataframe is head()
##this method return the header and a specified number of rows
import pandas as pd
df=pd.read_csv(r'c:\Users\divya\Downloads\pandas_practice_dataset.csv')      ##whole path
print(df.head(4))                #starting 4 rows of table
print(df.head())                 ##by default it printthe table

##tail 
df=pd.read_csv(r'c:\Users\divya\Downloads\pandas_practice_dataset.csv') 
print(df.tail(4))                 ## print last 4 rows of table

##what if you want information about the data in dataframe
##info()
import pandas as pd
df=pd.read_csv(r'c:\Users\divya\Downloads\pandas_practice_dataset.csv')      ##whole path
print(df.info())