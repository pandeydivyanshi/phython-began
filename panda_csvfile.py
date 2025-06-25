##read csv files:(CSV stands for comma seprated value)
##it is simply way to store big and biggest data sets
##csv file contain plain text.
##loading csv into dataframe with to string
import pandas as pd
df=pd.read_csv(r'c:\Users\divya\Downloads\pandas_practice_dataset.csv')      ##whole path
print(df.to_string())                      ##if rows are greater than 60 (it shows whole data set )

##loading csv into dataframe without to string
import pandas as pd
df=pd.read_csv(r'c:\Users\divya\Downloads\pandas_practice_dataset.csv')      ##whole path
print(df)                         ##it shows first 5 data and `last 5 data and middle data are dotted

##max rows: you can check your systems maximum row with
import pandas as pd
print(pd.options.display.max_rows)

##**YES we can increase maximum number of rows to display the entire dataframe
# import panda as pd
# pd.options.display.max_row = 100
# df=pd.read_csv(r'c:\Users\divya\Downloads\pandas_practice_dataset.csv')  
# print(df.to_string())