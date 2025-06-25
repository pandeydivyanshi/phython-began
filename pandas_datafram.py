##dataframe : it is 2D data structure like 2D array include row and column
import pandas as pd
data={"cal":[2332,324,2424],"dur":[45,56,43]}
x=pd.DataFrame(data)
print(x)

##locate row: pandas use the loc attribute to return one or more specified row
#(in form of series)
import pandas as pd
data={"cal":[2332,324,2424],"dur":[45,56,43]}
x=pd.DataFrame(data)
print(x.loc[0])

#rutrn row 0 and 1(in form of data frame)
import pandas as pd
data={"cal":[2332,324,2424],"dur":[45,56,43]}
x=pd.DataFrame(data)
print(x.loc[[0,1]])

##NAME INDEX:with index arrgument ,we can name our own index
import pandas as pd
data={"cal":[2332,324,2424],"dur":[45,56,43]}
x=pd.DataFrame(data,index=["d1","d2","d3"])
print(x)

##locate name index
import pandas as pd
data={"cal":[2332,324,2424],"dur":[45,56,43]}
x=pd.DataFrame(data,index=["d1","d2","d3"])
print(x.loc["d2"])

##output in dataframe
import pandas as pd
data={"cal":[2332,324,2424],"dur":[45,56,43]}
x=pd.DataFrame(data,index=["d1","d2","d3"])
print(x.loc[["d2","d3"]])

##load the data from csv file into dataframe i.e. data.csv
import pandas as pd
file=pd.read_csv('data.csv')
print(file)