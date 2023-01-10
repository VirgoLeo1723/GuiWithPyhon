from numpy import *
from numpy import linalg
from sympy import *
class matrix_operator:
    @staticmethod
    def plus(a,b):
        return add(a,b)
    @staticmethod    
    def multi(a,b):
        return dot(a,b)
    @staticmethod
    def pow(C,n):
        return linalg.matrix_power(C,n)
    @staticmethod
    def trans(A):
        return transpose(A)
    @staticmethod
    def eche_form(a):
        return Matrix(a).rref()[0]
    