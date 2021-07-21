# Ex.1 fib

# fib = [1, 1]
# for i in range(2, 20):
#   fib.append(fib[i - 1] + fib[i - 2])
# print(fib)

# Ex.2 perfect num

# res = []
# for i in range(3, 10001):
#   sum = 0
#   for j in range(1, i):
#     if i % j == 0:
#       sum += j
#       if sum > i:
#         break
#   # print(sum)
#   if sum == i:
#     res.append(i)
# print(res)


# Ex.3 find prime , linear sieve

# if i is a prime
isPrime = [1] * 100
# increasing , the list of prime
primes = []
# print(len(isPrime))
for i in range(2, 100):
  if isPrime[i]:
    primes.append(i)
  for j in range(len(primes)):
    # i = 6, primes = [2, 3, 5]
    if primes[j] * i > 99:
      break
    # print(i, j, primes)
    isPrime[primes[j] * i] = 0
    if i % primes[j] == 0:
      break
print(primes)

# 2 * 2 = 4
# 2 * 3 = 6 ... 2 * 50 = 100  are not prime isPrime[100] = 0
# 3 * 2 = 6 3 * 3 = 9 3 * 6 = 18 ... 3 * 33 = 99  isPrime[99] = 0
# ... 7 * .. 14 = 98 isPrime[98] = 0
# 3 * 6 = 18   2 * 9 = 18

# 2 * 3 * 3
# 3 * 2 * 3

# i = 6 2 * 6 12  6 % 2 == 0 3 * 6 18 6 * 5 = 30  2 * 3 * 3 2 * 9 2 * 3 * 5  2 * 15
# i = 9 


