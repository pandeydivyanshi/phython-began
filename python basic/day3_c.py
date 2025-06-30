## dicinory##
info = {
    "key": "value",
    "name": "divyanshi",
    "age": 20,
    "is_student": True,
    "courses": ["Python", "JavaScript", "C++"],
    "marks":[99,96,98],
    "height": 5.3,
}
print(info)
# Accessing values in a dictionary
print(info["name"])             # Accessing value by key
print(info.get("courses"))       

print(len(info))            # Length of the dictionary
print(type(info))          # Type of the dictionary
info["name"] = "divyanshi pandey"                     # assigning new value to key
print(info)
null_dic={}
print(null_dic)
null_dic["name"] = "dIVYANSHI"          #assiging key and value both
print(null_dic)

## nested dicenory##
inform={
    "name":"div",
    "feature" : {
        "age":20,
        "height" : 5.3,
        "weight" : 50,
    }
    }
print(inform)
print(inform.keys())                  # return all key of that decionary
print(inform.values())                # return all values of that decionary
print(inform.items())                 # resturn key and values
print(list(inform.keys()))            #type cast keys into list
print(inform.get("feature"))            # it return the value of given key

##update dict##
info = {
    "key": "value",
    "name": "divyanshi",
    "age": 20,
    "is_student": True,
    "courses": ["Python", "JavaScript", "C++"],
    "marks":[99,96,98],
    "height": 5.3,
}
newdit ={"place":"delhi","caste":"pandey"}                  ### updating by assiginig new dict new key and value
info.update(newdit)
print(info)
info.update({"origin":"sant kabir nagar"})                 ### updating direct new key and value
print(info)
info.update({"name":"rajanidivyanshi pandey"})             # it only update value of key
print(info)
