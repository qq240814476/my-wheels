import math

# in -> cm, 1in = 2.45cm
# Ex. 1
inNum = float(input("Input in number: "))
print("revert to centimeter: " + str(inNum * 2.45))

# Ex.2
score = int(input("Input the score, pls: "))
if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
elif score >= 60:
  print("D")
else:
  print("E")

# exercise 3
num = int(input("Input some number: "))
def isPrime(num):
  if num == 2:
    return "Yes"
  elif num < 2:
    return "No"
  for i in range(3, math.ceil(math.sqrt(num))):
    if num % i == 0:
      return "No"
  return "Yes"
isP = isPrime(num)
print("Is prime?  " + isP)