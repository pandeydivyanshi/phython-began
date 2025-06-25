## pandas series is like column in table,it is 1D array which holds data of any type.
##here we wii create a simple pandas series
import pandas as pd
x=[1,2,34,5,6,7,9]
y=pd.Series(x)
print(y)

#labeling -label can use to access a specified value
import pandas as pd
x=[1,2,34,5,6,7,9]
y=pd.Series(x)
print(y[2])


##with create labels we can create our own labels(we can change indexing by anything like alphabets)
import pandas as pd
x=[1,2,34,5,6,7,9]
y=pd.Series(x,index=["a","b","c","d","e","f","g"])
print(y)

## labeling -label can use to access a specified value(after creating own labels)
import pandas as pd
x=[1,2,34,5,6,7,9]
y=pd.Series(x,index=["a","b","c","d","e","f","g"])
print(y["d"])

##we can also use a key or value object like a dictionary , when creating a series
##here we will create a simple pandas series from a dictionary
import pandas as pd
cal={"d1":333,"d2":389,"d3":420}
z=pd.Series(cal)
print(z)

## now we will create a series using only data from d1 and d2
import pandas as pd
cal={"d1":333,"d2":389,"d3":420}
aar=pd.Series(cal,index=["d1","d2"])
print(aar)

##DATAFRAMS:data sets in pandas are usually mutidimensional tabels,called data frames
#series are like columns and datafram is whole table
##we will create a data fram from 2 series
import pandas as pd
x={'cal':[430,465,355],"duration":[50,40,45]}
y=pd.DataFrame(x)
print(y)