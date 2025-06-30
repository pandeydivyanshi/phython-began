##wrong DATA:its only a wrong data


##loading original data
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
print(x.to_string()) 

##here we  will det age =45 in row 3
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
x.loc[3,"Age"]=45
print(x.to_string()) 

## for laeger data set : now we will loop through all values in "Age" column ,
#if value is higher than 60 than set it to 60
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
for i in x.index:
    if x.loc[i,"Age"]>60:
        x.loc[i,"Age"] = 60
print(x.to_string())

##we can also remove rows for wrong data in largest dataset
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
for i in x.index:
    if x.loc[i,"Age"]>60:
        x.dropna(i,inplace=True)
print(x.to_string())