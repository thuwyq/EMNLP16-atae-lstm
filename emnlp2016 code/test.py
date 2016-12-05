import numpy as np

n = 4

a = np.random.random((n,n))
# print a
for i in range(n):
    a[i][i] = 1
    for j in range(n):
        a[i][j] = a[j][i]
    
b = np.array(np.mat(a).I)

print a
print b

print np.dot(a, b)
