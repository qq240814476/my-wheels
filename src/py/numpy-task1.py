import numpy as np

# ex.1
res = np.array([[1], [1,1], [1,2,1], [1,2,2,1], [1,2,4,2,1]])
# for i in range(1,6):
#   n = 1
#   res[i].append(1)
#   while n < i:
#     if n == i-1:
#       res[i].append(1)
#       n+=1
#       break
#     res[i].append(res[i-1][n - 1] + res[i-1][n])
#     n+=1
print(res)

# ex.2
def mergeSort(fir, sec):
  res = np.append(fir, sec)
  res = np.sort(res)
  print(res)
mergeSort([1,2,3], [2,4,5])