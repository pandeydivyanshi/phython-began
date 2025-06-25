##JSON:big data sets are normally storted and extracted as json
#json is plain text,but it has a format of an object
##loading the json into dataframe
import pandas as pd
x=pd.read_json(r'c:\Users\divya\Downloads\students.json')
print(x.to_string())

#dictinoary as a JASON:if your json code is not in a file but in python dictinoary,then you can do all below
import pandas as pd
data =[
  {
    "id": 1,
    "name": "Alice",
    "age": 22,
    "department": "Computer Science",
    "score": 85.5,
    
  },
  {
    "id": 2,
    "name": "Bob",
    "age": 21,
    "department": "Mathematics",
    "score": 78.0,
    
  },
  {
    "id": 3,
    "name": "Charlie",
    "age": 23,
    "department": "Statistics",
    "score": 66.5,
    
  },
  {
    "id": 4,
    "name": "David",
    "age": 20,
    "department": "Physics",
    "score": 45.0,
    
  },
  {
    "id": 5,
    "name": "Eve",
    "age": 22,
    "department": "Economics",
    "score": 90.0,
    
  }
]
y=pd.DataFrame(data)
print(y)