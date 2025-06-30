##cleaning data:it means fixing bad data in our data set
##bad data:empty cell ,data in wrong formate,duplicate data and wrong data
##empty cell: it will give wrong result always,we will have to remove the rows always that contain bad data

##loading the data
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
print(x.to_string())       #to_string() will print the whole dataframe

 
##removing empty cells(cleaning data)
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
new=x.dropna()        #dropna() will remove the rows that contain empty cells
print(new.to_string())  #to_string() will print the whole dataframe

##if at any case we want to change the original dataframe then we can use inplace=True
##it will remove the rows containing NULL(NaN) values
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
x.dropna(inplace=True)  #inplace=True will change the original dataframe
print(x.to_string())  

##replacing the empty values:we will use fillna() function to replace the empty values with some value
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
x.fillna(0,inplace=True)  #fillna() will replace the empty values with 0
print(x.to_string())  

##to replace only empty value for one column, we need to specify the column name
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
x["Gender"].fillna(0,inplace=True)  #fillna() will replace the empty values with 0
print(x.to_string())  

##here we can also replace the empty cell using mean(),median()or mode()
##calculate the mean and replace the empty value with it
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
z=x["Age"].mean()
x["Age"].fillna(z,inplace=True)  #fillna() will replace the empty values with 0
print(x.to_string()) 

##with meadian
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
z=x["Age"].median()
x["Age"].fillna(z,inplace=True)  #fillna() will replace the empty values with 0
print(x.to_string()) 

##with mode
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
z=x["Age"].mode()
x["Age"].fillna(z,inplace=True)  #fillna() will replace the empty values with 0
print(x.to_string()) 