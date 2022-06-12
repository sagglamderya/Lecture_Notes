import numpy as np
x=np.array([1,2,3]) #creates a numpy array
y=np.array([1,2,3], dtype=str) #returns ints into str
z=np.array(['1','2','3'], dtype=int) #reutns strs into int
a=np.zeros(8) #returns you an array with 8 zeros which are float
b=np.zeros(8, dtype=str) #if you specify data type with str it gives you 8 empty strs, also you can use int32 dtype
c=np.zeros((3,5)) #returns you 2 dimensional array with 3 lines and 5 columns
d=np.zeros((3,5), dtype=int) #you can also use other dtypes here
e=np.zeros([3,5,6]) #it gives you 3 dimensional array with 5 lines, 6 colums, 3 times. You dont have to use '[]', you can also use just double'()'
f=np.zeros([3,5,6], dtype=bool) #you can also use other dtypes here. 0 means False, 1 means True
l=np.full((3,4,5),5, dtype=int) #you can create not empty list with '.full'. All features are same with '.zeros'. This is a 3 dimensional array with 3 depth, 4 lines, 4 columns and element of 5
l=np.full((3,4,5), "a")
q=np.full(4,5) # array with 4 elements of 5
q=np.arange(4,9)# returns elements from 4 to 9, 9 is not included. Not supported for str and float and bool
q=np.arange(2,12,2) # returns elements 2 to 12 by twos
q=np.arange(12,2,-2)# returns elements 2 to 12 by backward twos
q=np.linspace(1,2) #returns elements 1 to 2 with 50 elements (50 is default) and equal intervals. 1 and 2 are included
q=np.linspace(1,2, num=3) #returns elements 1 to 2 with 3 elements. 1 and 2 are included. You don't have to write "num=", you also can write only q=np.linspace(1,2,3)
q=np.linspace(1,2,3,endpoint=False) #if you don't want to include endpoint you can use ", endpoint=False"
q=np.linspace(1.4,2.3,4) #you can use floats instead of integars as well
#creating an random array
x=np.random.randint(1,10, (3,4)) #returns a random array with elements from 1 to 10 (10 is not included). In size of 3 lines and 4 columns
x=np.random.randint(1,10, (3,4,5)) #also can be used for 3 dimensional arrays. Returns an random array with elements from 1 to 10 and size is 3 depth, 4 lines, 5 colıumns
x=np.random.randint(1,8) #returns a random number 