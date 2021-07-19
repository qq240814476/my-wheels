# strs = ['1+1', '10+10', '5+5']
# strs2 = ['2+2', '3+3', '12+12']
# for s in strs:
#   print(s.ljust(10, ' '), end='')
# print('')
# for s in strs2:
#   print(s.ljust(10, ' '), end='')

# Ex.1
# print(f'{fir}*{sec}={res}'.ljust(10, ' '), end=es)
# print('{}*{}={}'.format(i,j,j*i).ljust(10, ' '), end=es)

for i in range(1, 10):
  for j in range(1, i+1):
    k = j * i
    es = '\n' if j == i else ' ' 
    print(f'{j}*{i}={k}'.ljust(10, ' '), end=es)
