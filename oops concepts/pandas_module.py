#Pandas is the most popular library used for Data Analysis and Data Manipulation. Using Pandas, we can work on different types of data like 
#• Matrix Data with rows and columns • Unlabelled data • Heterogeneous types of data in tabular form • Statistical Data Sets 
'''import pandas as pd 
s = pd.Series() 
print(s)'''
'''import pandas as pd 
import numpy as np 
arr = np.array([1,2,3,4,5]) 
s = pd.Series(arr) 
print(s) 
import pandas as pd
list1 = [9,10,11,12,13,14] 
s = pd.Series(list1) 
print(s)  
import pandas as pd
dict1 = {'a':0,'b':1,'c': 2} 
s = pd.Series(dict1) 
print(s) 
s = pd.Series(6, index= [0,1,2,3]) 
print(s) 
data = ["Tokyo","Olivia","Denver","Nairobi"] 
data1=["Prudhvi","Theja","Marcus"]
s = pd.Series(data, index= ['a','b','c','d'])
s1 = pd.Series(data1, index= ['a','b','c']) 
print(s)
print(s1)
print(s[0],s1[0])
print(s[3:],s1[2:])
print(s[:-2])
print(s1[:-1])
print(s['d'])
print(s1['c'])
print(s[['a','c']])
s1 = pd.Series(['Emiley','Homes']) 
s2 = pd.Series([1,2]) 
print(s1.append(s2)) 
print(s1.append(s2,ignore_index = True)) 
#print(s1.append(s2,ignore_index = True,verify_integrity=True)) 
#print(s1.append(s2,verify_integrity=True)) 
import pandas as pd 
import numpy as np 
s = pd.Series([15,27,18,24,12,22]) 
print(s.apply(lambda x: x >= 20 and x <=25)) 
print(s.apply(lambda x: x*2)) 
import pandas as pd 
import numpy as np 
s = pd.Series([15,27,np.nan,24,None,22]) 
print(s.backfill()) 
print(s) 
print(s.backfill(inplace=True)) 
print(s)'''
#DATA FRAME 
#Data Frame is a two-dimensional labelled array capable of holding data of any type (integer, 
#string, float, python objects, etc.). Data is aligned in a tabular fashion of Rows and Columns. 
#Syntax: pandas.Series( data, index, columns, dtype) 
#data – can be of lists/ndarray/dictionaries 
#index – must be unique and is used for row labels. Default value in np.arange(n) 
#columns –Default value of np.arange(n) is for columns if no index value is passed. 
#dtype – declare the data type we want to represent for each column 
import pandas as pd 
df = pd.DataFrame() 
print(df) 
import pandas as pd 
data = [1,2,3,4,5] 
df = pd.DataFrame(data) 
print(df) 
import pandas as pd 
data = [['Alex',10],['Bob',12],['Clarke',13]] 
df = pd.DataFrame(data,columns=['Name','Age']) 
print(df) 
import pandas as pd 
data={'Name':['Professor','Berlin','Lisbon','Rio','Helsinki','Oslo','Stockholm','Bogota'], 
'Marks':[98,94,89,82,85,83,77,80]} 
df = pd.DataFrame(data) 
print(df) 
import pandas as pd 
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}] 
#With two column indices, values same as dictionary keys 
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b']) 
#With two column indices with one index with other name 
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1']) 
print(df1) # creating df with given keys in dictionary 
print(df2) # creating df with one key different from given list of keys so will result NaN 
import pandas as pd 
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])} 
df = pd.DataFrame(d) 
print(df)  
