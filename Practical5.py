#LAB PP Q5 a
import numpy as np

# x = np.array([[17, 24, 1, 8, 15], 
#             [23, 5, 7, 14, 16],
#             [ 4, 6, 13, 20, 22],
#             [10, 12, 19, 21, 3],
#             [11, 18, 25, 2, 9]])

m = []
for i in range(int(input())):
    m.append([int(x) for x in input().split()])

x = np.array(m)

#Direct Computation
# Sum of Rows
rs = [x[i].sum() for i in range(x.shape[0])]
print("Row Sum: "+str(rs))

# Sum of Columns
x = x.T
rs = [x[i].sum() for i in range(x.shape[1])]
x = x.T
print("Column Sum: "+str(rs))

#Sum of Digonal 1 and 2
dig = []
dig.append(x.diagonal().sum())
x = np.rot90(x,3)
dig.append(x.diagonal().sum())
print("Digonal Sum: "+str(dig))

print()

#Maima and minima
rs = [x[i].sum() for i in range(x.shape[0])]
print("Row Sum Maxima {} and Row Sum Minima {}".format(max(rs),min(rs)))

# Sum of Columns
x = x.T
rs = [x[i].sum() for i in range(x.shape[1])]
x = x.T
print("Column Sum Maxima {} and Column Sum Minima {}".format(max(rs),min(rs)))

#Sum of Digonal 1 and 2
dig = []
dig.append(x.diagonal().sum())
x = np.rot90(x,3)
dig.append(x.diagonal().sum())
print("Digonal Sum: "+str(dig))

print("YES" if(list(set(dig))[0]==max(rs)==min(rs)) else "NO")

