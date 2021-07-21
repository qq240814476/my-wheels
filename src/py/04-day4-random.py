# 100 random char and record the number of each  appear char
import string as st
import random
chars = st.ascii_letters + st.digits + st.punctuation

randomChars = ''
for i in range(0, 100):
  randomChars += random.choice(chars)
res = {}
for i in range(0, 100):
  if res.get(randomChars[i]):
    res[randomChars[i]] += 1
  else:
    res[randomChars[i]] = 1
print(res)
