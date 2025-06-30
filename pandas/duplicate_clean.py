##removing duplicates values : 1st we need to discover them VIA duplicated() fnc
##loading original data
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
print(x.to_string()) 


##returns TRUE for every row that is duplicate otherwise return false
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
print(x.duplicated())

##removing duplicates from data set Via drop_duplicates()
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
x.drop_duplicates(inplace=True)
print(x.to_string()) 