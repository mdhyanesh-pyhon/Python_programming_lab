import numpy
lst = [1,2,3,5,6]
l2 = [4,5,6,8,9]
a_l1=numpy.array(lst)
b_l2=numpy.array(l2)
print(f"Sum of two arrays are {a_l1+b_l2}")
print(f"subtraction of two arrays {a_l1-b_l2}")
print(f"Multiplication of two arrays {a_l1*b_l2}")
print(a_l1[0:3])
print(a_l1[0:6:2])
print(a_l1[0::3])
print(a_l1[::])
print(a_l1[6::-1])

