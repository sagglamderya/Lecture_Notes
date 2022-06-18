import numpy as np
x=np.array([1,2,3]) #creates a numpy array
y=np.array([1,2,3], dtype=str) #returns ints into str
#x*y #multiplies elements of arrays and returns a new array with elements of 1*1, 2*2, 3*3. Both arrays should have equal numbers of elements.
#x+y #sum both arrays and returns a new array [1+1,2+2,3+3]
#x*3 #multiplies array and returns a new array [1*3,2*3,3*3] but x array stays same 
#x*3 #if ypu want to change the array you should write like this
z=np.array(['1','2','3'], dtype=int) #returns strs into int
a=np.zeros(8) #returns you an array with 8 zeros which are float
b=np.zeros(8, dtype=str) #if you specify data type with str it gives you 8 empty strs, also you can use int32 dtype
c=np.zeros((3,5)) #returns you 2 dimensional array with 3 lines and 5 columns
d=np.zeros((3,5), dtype=int) #you can also use other dtypes here
e=np.zeros([3,5,6]) #it gives you 3 dimensional array with 5 lines, 6 colums, 3 times. You dont have to use '[]', you can also use just double'()'
f=np.zeros([3,5,6], dtype=bool) #you can also use other dtypes here. 0 means False, 1 means True
l=np.full((3,4,5),5, dtype=int) #you can create not empty list with '.full'. All features are same with '.zeros'. This is a 3 dimensional array with 3 depth, 4 lines, 4 columns and element of 5
l=np.full((3,4,5), "a")
l.shape # returns the shape of l--> 3,4,5
l.ndim #returns dimension number of l--> 3
l.size #ruturns size of l (how many elements l has)--> 3*4*5-->60
l.dtype #returns data type of elements of l--> string
q=np.full(4,5) # array with 4 elements of 5
q=np.arange(4,9)# returns elements from 4 to 9, 9 is not included. Not supported for str and float and bool
q=np.arange(2,12,2) # returns elements 2 to 12 by twos
q=np.arange(12,2,-2)# returns elements 2 to 12 by backward twos
#q.reshape(2,3) #makes q array 2 dimensional with 2 lines and 3 columns but q should have 6 elements. q array stays same
#q.reshape (-1,2) #if you type -1 it decides what it should be. ex: if you have 6 elements it will give 3,2 
q=np.linspace(1,2) #returns elements 1 to 2 with 50 elements (50 is default) and equal intervals. 1 and 2 are included
q=np.linspace(1,2, num=3) #returns elements 1 to 2 with 3 elements. 1 and 2 are included. You don't have to write "num=", you also can write only q=np.linspace(1,2,3)
q=np.linspace(1,2,3,endpoint=False) #if you don't want to include endpoint you can use ", endpoint=False"
q=np.linspace(1.4,2.3,4) #you can use floats instead of integars as well
#creating an random array
x=np.random.randint(1,10, (3,4)) #returns a random array with elements from 1 to 10 (10 is not included). In size of 3 lines and 4 columns
x=np.random.randint(1,10, (3,4,5)) #also can be used for 3 dimensional arrays. Returns an random array with elements from 1 to 10 and size is 3 depth, 4 lines, 5 colıumns
x=np.random.randint(1,8) #returns a random number 
x=np.eye(3,4) #creates an 2-dimensional array with elements of 0 and 1. every line has one 1.
x=np.array([1,2,3])
y=np.array([4,5,6])
l=[7,8,"9.1"] #l can be tuple as well: l=(1,2,3)
z=np.concatenate([x,y,l]) #combine x and y arrays, also you can combine with lists. If an array or list in this combination has float elements your combination will be elements of floats, same for str elements
#if you try to concatenate two arrays with different shapes it will return an error
x=np.array([2,3,5,8])
y=np.zeros((4,3))
#z=np.concatenate([x,y])  #Error: all the input arrays must have same number of dimensions
z=np.concatenate([y,y], axis=1) #if you type axis=1 it will combine same array in a way that it repeat in right not below
# output:
# [[0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0. 0.]]
z=np.concatenate([y,y])
#output:
# [[0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]]
y=np.array([5,8,6,5])
z=np.concatenate([x,y])#normally these x and y arrays do not have a shape and if you concatenate these arrays it will return a single line of array combination.
#output if you use concantenate:
#[2 3 5 8 5 8 6 5]
#but with stack, it will return them with different columns 
#output:
#[[2 3 5 8]
# [5 8 6 5]]
l=[0,1,2,3,4,5,6,7,8,9]
z=np.split(l, [4,6]) #it will split your list or array between 3rd and 4th elements and 5th and 6th elements as arrays. more than 2 slices can be used
#output:
#[array([0, 1, 2, 3]), array([4, 5]), array([6, 7, 8, 9])]
m,r,b=np.split(l, [4,6])
#print(m,r,b) output:
#[0 1 2 3] [4 5] [6 7 8 9]
a=np.arange(20).reshape(2,10)
#[[ 0  1  2  3  4  5  6  7  8  9]
# [10 11 12 13 14 15 16 17 18 19]]
z=np.vsplit(a,[1])
#[[ 0  1  2  3  4  5  6  7  8  9]
#-------------------------------->split from here (vertically) (from 1st line)
# [10 11 12 13 14 15 16 17 18 19]]
z=np.vsplit(a,[1])[0] #this is in list format you can access 0th index as well
#[[0 1 2 3 4 5 6 7 8 9]]
z=np.hsplit(a, [4,7])
#[[ 0  1  2  3 | 4  5  6 | 7  8  9]
# [10 11 12 13 |14 15 16 |17 18 19]]
#              !         !
#            split from there
#output:
#[array([[ 0,  1,  2,  3],
#       [10, 11, 12, 13]]), array([[ 4,  5,  6],
#       [14, 15, 16]]), array([[ 7,  8,  9],
#       [17, 18, 19]])]
z=np.hsplit(a, [4,7])[0] 
#output:
#[[ 0  1  2  3]
# [10 11 12 13]]
z=np.sort(y) #it sorts your array smallest to biggest
#output:[5 5 6 8]
z=np.argsort(y) #sorts your array and gives indexes of these elements
#original array->[5,8,6,5] , sorted version of it->[5 5 6 8]
#output:[0 3 2 1]

### fancy indexing ###
x=np.arange(1,15)
idx=[4,5,7,1] #indexes which you want to return
#print(x[idx])
#output:[5 6 8 2]
x=np.arange(15).reshape(3,5)
x[0:2,2:4]
# -  - - -  - - -
# 0  1 | 2  3 | 4 
# 4  6 | 7  8 | 9 
# -  - - -  - - - 
# 10 11| 12 13| 14
#output:[[2 3]
#        [7 8]]
x[1, [3,4]] #2nd lines 4th and 5th indexes
#output:[8 9] 
x[0:, [3,4]] #returns every lines 4th and 5th columns
#output: [[ 3  4]
#         [ 8  9]
#         [13 14]]
idx1=[1,0,2]
idx2=[3,0,2]
x[idx1,idx2] #output: [ 8  0 12]

#   changing indexes   #
y=np.arange(19)
y[[2,5,8,1,6]]=15 #2,5,8,1,6th indexes are 15 now outout: [ 0 15 15  3  4 15 15  7 15  9 10 11 12 13 14 15 16 17 18]
x=np.arange(1,21).reshape(4,5)
y=x[:2,:3].copy() #output: [[1 2 3] -->copy() copies a list. since y is a sublist if you change an index in y this index is also changed in x. if you do not want to affect x array you can copy subarray y.
#                           [6 7 8]]

### conditional indexing ###
x=np.arange(1,10)
x<5 #looks indexes of x for being <5. if yes returns true -> output:[ True  True  True  True False False False False False]
x[x<5] #looks indexes of x and returns the elements which are <5 --> output:[1 2 3 4]
y=np.array([1,5,7,6,2,7,9,8,4])
x==y #looks if these array values in same indexes are equal or not ->output:[ True False False False False False False  True False] !arrays should have equal numbers of elements
x[x==y] #returns the values of x which are equal with y ->output:[1 8]
(x<3)|(x>5) # "|" means "or" ->output: [ True  True False False False  True  True  True  True]
(x<3) & (x>1) # "&" means "and" ->output: [False  True False False False False False False False]
x[(x<3)|(x>5)] #output:[1 2 6 7 8 9]
~(x>4) # "~" means "not" ->output:[ True  True  True  True False False False False False]
np.sum(x) # sums all elements of x
np.sum(x<5) #counts elements which are smaller than 5 ->output: 5
np.sum(x[x<5]) #sums elements of x which are smaller then 5
x=np.arange(20).reshape(4,5)
np.sum(x, axis=0) #sums elements of x which are in same line and returns their value in an array. if axix=1 it would sums elements in same column ->output:[30 34 38 42 46]
np.all(x>-1) #looks all elements of x and returns true if all of them are bigger then -1. vice versa is valid with false ->output:True
np.all(x<5, axis=1) #looks all elements of x by columns -> output: [ True False False False]
np.any(x<5, axis=0)#looks all elements of x and returns true if any of them is smaller then 5 by lines.-> output:[ True  True  True  True  True]


 