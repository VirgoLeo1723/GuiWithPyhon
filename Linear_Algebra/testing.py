from numpy import *

A=[[1,2,2],[2,3,4],[3,4,5]]
B=[[2,3,4],[2,3,5],[3,5,6]]
C=[1,2,3,4]
D=add(A,B)
print(D[1])
print(D.shape[0],",",D.shape[1])
print(add(A,B))
print(multiply(A,B))
print(power(C,2))
print(A)
print(transpose(A))