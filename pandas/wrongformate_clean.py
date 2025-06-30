##data in wrong formate :to fix this problem >2 ways
##removing the rows or convert all the cell in same formate
##loading original data
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
print(x.to_string())

#now lwts try to convert all cells in the date columns into dates
##via to_datetime()
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
x["JoinDate"] = pd.to_datetime(x["JoinDate"], errors='coerce')  #errors='coerce' will convert invalid parsing to NaT
print(x.to_string())

##we will remove the rows that contain NaT values in JoinDate column
import pandas as pd
x=pd.read_csv(r'c:\Users\divya\Downloads\data_cleaning_sample_100.csv')
x["JoinDate"] = pd.to_datetime(x["JoinDate"], errors='coerce')  #errors='coerce' will convert invalid parsing to NaT
x.dropna(subset=["JoinDate"], inplace=True)  #dropna() will remove the rows that contain NaT values
print(x.to_string())