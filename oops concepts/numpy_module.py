#NUMPY • Numpy stands for NUMerical Python.  • It is a library that is used to work with N-dimensional Arrays. • Arrays are data structure that allows us to store multiple values into single variable. • Numpy gives us efficient way of storing and manipulating numerical data. • Numpy has many built-in functions which used to perform mathematical operations. 
#Installing Numpy: pip install numpy 
#Importing Numpy: import numpy as np 
#Advantage: • As lists can be heterogeneous it occupies more memory, Lists store the Object value, 
#object data type, Reference count and Size of data item. • Arrays on other hand have faster execution/access as they occupy less memory and 
#are homogeneous. They have type of int32/int16/int8. • Numpy arrays are used to store data in multi-dimensional structure. 
#Array: • Numpy Array is a grid of values of homogeneous data items indexed by tuple of non
#negative integers. • Rank of the array: No. of dimensions in array • Shape of the array: Tuple of integers giving size of array along each dimension.   
import numpy as np 
#1.creating numpy one dimension array. checking type and size. 
'''a=np.array(1)
print(a)
print(type(a))#Shows type of variable-<class 'numpy.ndarray'>
print(a.size)#length of an array'''
#2.Creating 1d array 
'''a = np.array([1,2,3]) 
print(a) 
print(type(a)) 
print(a.shape) 
print(a.ndim)'''
#3.Creating 2d array 
'''a = np.array([[1,2,3], [4,5,6]]) 
print(a) 
print(type(a)) 
print(a.shape) 
print(a.ndim)'''
#4.Creating 3d array 
'''a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 
print(a) 
print(type(a)) 
print(a.shape) 
print(a.ndim)'''
#dtype: Inbuilt function use dtype declare data types and to find data type of given data item.  
'''a = np.array([1,2,3,4.2,5],dtype = 'int32')
print(a.dtype) 
print(a) 
a = np.array([1,2,3,2,44,5.2]) 
print(a) 
print(a.dtype)
b = np.array([1.0,2.0,3.0]) 
print(b) 
print(b.dtype)'''
#arange: create an array of number in given range,reshape: reforming arrays by changing their dimensions,itemsize: returns length of each element of array in bytes  
'''a = np.arange(20) 
print(a) 
print(a.reshape(4,5)) 
print(a.itemsize) 
b = np.arange(5,20) 
print(b) 
print(b.reshape(5,3)) 
print(b.itemsize)''' 
'''#zeros: returns a new array of specified size filled with zeroes. 
x = np.zeros([3,2], dtype = int)  
print(x) 
#ones: returns a new array of specified size filled with ones.
x = np.ones([3,2], dtype = int)  
print(x) 
#full: returns a new array of specified size filled with specified mentioned value.
x = np.full([4,4],33,dtype=int)  
print(x) 
#eye: returns a new array of specified size filled of Identity Matrix. 
x = np.eye(5, dtype = int)  
print(x) 
#random.random: returns a new array of specified size filled with random values. 
x = np.random.random([3,4])  
print(x)
#Practice Example  
out1 = np.ones((7,7),dtype=int) 
print(out1) 
r = np.zeros((5,5)) 
r[3,2]=9 
print(r) 
out1[1:6,1:6] = r 
print(out1) '''
#Accessing Elements of an array 
z = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]]) 
print(z)
#to find specific element 
print(z[0,6])
#to get specified row 
print(z[0,:])
#to get specified column 
print(z[:,5])
#to get entire array using splicing  
print(z[:,:]) 
#indexing & slicing 
print(z[:2,4:])
a = np.array([[1,2], [3, 4], [5, 6]]) 
print(a)
print(a[[0, 1, 2], [0, 1, 0]]) 
print(np.array([a[0, 0], a[1, 1], a[2, 0]])) 
print(np.array([a[0, 1], a[0, 1]]))
#Mutate one element from each row of matrix 
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) 
print(a) 
b = np.array([0, 2, 0, 1]) 
print(a[np.arange(4), b]) 
a[np.arange(4), b] += 10 
print(a)
#Boolean Indexing: Returns boolean value depending on condition 
a = np.array([[1,2], [3, 4], [5, 6]]) 
bool_idx = (a > 2) 
print(bool_idx) 
print(a[bool_idx]) 
#(or) 
print(a[a > 2])  
#Mathematical operations – Can perform mathematical operations on array 
a = np.array([10,20,30,40,50]) 
print(a*2) 
print(a/2) 
print(a//2) 
print(a+2) 
print(a-4) 
#copy: can copy an array by assigning to a variable 
a = np.array([10,20,30,40,50]) 
b = a.copy() 
b[3] = 100 
print(a) 
print(b) 
#sort: sort the elements in array 
a = np.array([22,20,49,31,43]) 
a.sort() 
print(a) 
#concatenate: add two arrays into a single array 
a = np.array([1, 2, 3, 4]) 
b = np.array([5, 6, 7, 8]) 
print(np.concatenate((a,b))) 
c = np.array([[1, 2],[3, 4]]) 
d = np.array([[5, 6],[7, 8]]) 
print(np.concatenate((c,d),axis = 0)) 
print(np.concatenate((c,d),axis = 1)) 
#max()-Maximum element disply.min()- Maximum element disply.sum()-Display of all elements in a array
print("Max:",a.max(),"Min:",a.min(),"Sum:",a.sum())
#flatten()-Display array in single line 
print("Before Falttern:",c)
print("After Falttern:",c.flatten())
#ravel()The numpy.ravel() functions returns contiguous flattened array(1D array with all the input-array elements and with the same type as it).
print("Before Ravel:",c)
print("After Ravel:",c.ravel())
#transpose() function changes the row elements into column elements and the column elements into row elements. The output of this function is a modified array of the original one.
print(c.transpose())
print(np.split(a,4))#We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
print(np.stack(b,axis=0))
print(np.resize(a,6))
print(np.where(a>2))
x = np.arange(8.0)
print(x)
print(np.array_split(x, 3))
print(np.array_split(x, 4))
print(np.unique([1, 1, 2, 2, 3, 3]))
A = np.arange(8).reshape((2,2,2))
print(A)
print(np.flip(A, 0))
print(np.flip(A, 1))
print(np.flip(A))
print(np.flip(A, (0, 2)))
A = np.random.randn(3,4,5)
print(np.all(np.flip(A,2) == A[:,:,::-1,...]))