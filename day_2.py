##STRING##
str1="hellow guys.\nthis is day 2 of lecuture of python."                              #\n is use for next line
str2="hi everyone.\tgo with the flow."                                                 #\t is for tab space
print(str1)
print(str2)

##concatination ##                         
##imply addition of string use of + symbol##
str3=str1+str2
print(str3)
print(str1+str2)                                                    #add of two string
 ## finding length
print(len(str1))
print(len(str2))
print(len(str3))
str4=str3+"   "
print(len(str4))                                                          ##"" imply empty string

###indexing###
str="divyanshi pandey"
print(str[0])                                            #it gave d
print(str[5])                                            #it gave n 
print(str[8])                                            #it gave i
print(str[9])                                            #it gave space
print(str[15])                                           #it gave y
##print(str[16])                                           #it gave error b/c our range is 15 

##slicing##
##break the string into smaller part##
print(str[0:5])                                       ##it only consider index 01234 not 5 ,always in each case it will not include last index
print(str[:5])                                        ##in code line 30,31 it will start from index 0
print(str[5:15])
print(str[5:])                                         ##in code line 33,34 it start from index 5 and go till end
print(str[5:len(str)])

##negative indexing##
##it start from end of string##
print(str[-1])                                        ##it gave y
print(str[-14:-3])                                     ##it start from -14 and go till -4 not include -3

##string function##
str="divyanshi pandey"
print(str.endswith("an"))                              ##str.endswith("an") check whether string end with "an" or not ,it return boolean value(True/False)
print(str.capitalize())                                ##it capitalize first letter of string  , it does not change original string 
str=str.capitalize()                                  ##it change original string
print(str)                                             ##it print string after capitalizing first letter
print(str.replace("i","ee"))                        ##it replace i with ee in string     
print(str.replace("pandey","pandit"))                      
print(str.find("n"))                               ##it find index of first occurence of n in string
print(str.find("u"))                              ##it return -1 if character is not present in string 
print(str.count("i"))                               ##it count occurence of i in string
print(str.count("e"))                               ##it count occurence of e in string

##practice##
name=input("Enter your name: ")                        
print("Hello "+name+" welcome to python lecture")        
print("lenth of name is ",len(name))
print("occurance of letter e in name is ",name.count("e"))
