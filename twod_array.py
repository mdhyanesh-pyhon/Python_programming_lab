import numpy as np
l1 = [[1,2,3],[4,5,6]]
l2 = [[7,8,9],[1,2,3]]
a_l1 = np.array(l1)
b_l2 = np.array(l2)
sum = a_l1+b_l2
print("Sum of two arrays")
for i in range(0,len(sum)):
    print(sum[i])
print("Subtraction of two arrays")
sub = a_l1-b_l2
for i in range(0,len(sub)):
    print(sub[i])
print("Multiplication of two arrays")
mul = a_l1*b_l2
for i in range(0,len(mul)):
    print(mul[i])




