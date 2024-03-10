# In this we are going to deal with the basic of tensorFlow

import tensorflow as tf # importing tensorflow

# we can declare variable with different datatypes like ex:--

stringg = tf.Variable("Hi Coder! Welcome to Python",tf.string)
num = tf.Variable(125,tf.int32)
print(stringg) 
print(num) 
#This is the way to declare the variables... there are more datatypes will explore afterwards

# RANK: There are Ranks/Degree in tensorflow:

rank1_tensor=tf.Variable(["Hello"],tf.string)
rank2_tensor=tf.Variable([["Pinku","Modi","is","coder"],["we","are","using","string"]],tf.string)

print(tf.rank(rank1_tensor))
print(tf.rank(rank2_tensor)) # The rank of a tensor is direclty related to the deepest level of nested lists

# let's talk about SHAPE of tensorflow: 

# The shape of a tensor is simply the number of elements that exist in each dimension
print(rank2_tensor.shape)

#changing of a Shape: 
tensor1 = tf.ones([1,2,3]) #this will print the shape with the value 1s as an element but we can use tf.fill to get the value what we want  for example:
tensorr=tf.fill([1,2,3],3.2)
print(tensorr)
print(tensor1)  # tf.ones() creates a shape [1,2,3] tensor full of ones
tensor2 = tf.reshape(tensor1, [2,3,1])
print(tensor2)  # reshape existing data to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3, -1])  # -1 tells the tensor to calculate the size of the dimension in that place
                                        # this will reshape the tensor to [3,2]
                                                                             
# The numer of elements in the reshaped tensor MUST match the number in the original


# we can create matrix in tensorflow and add it as a variable ex:

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] #defining a matrix

# storting it to a variable
tenn=tf.Variable(matrix, dtype=tf.int32)

print(tf.rank(tenn))
print(tenn.shape)

# we can also do slicing in this 
# Now lets select some different rows and columns from our tensor

three = tenn[0,2]  # selects the 3rd element from the 1st row
print(three)  # -> 3

row1 = tenn[0]  # selects the first row
print(row1)

column1 = tenn[:, 0]  # selects the first column
print(column1)

row_2_and_4 = tenn[1::2]  # selects second and fourth row, REMEMBER :: this will jump the step like (a::b)--> a is the row and the step it will jump to will be b
print(row_2_and_4)

column_1_in_row_2_and_3 = tenn[1:3, 0] #in python slicicng is done as (a,b) starting from row 1 to row 2 that isw upto b but not including b itself
print(column_1_in_row_2_and_3)