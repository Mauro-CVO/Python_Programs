
from math import gcd
a = [2, 3, 5]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
  lcm = lcm*  i/ gcd(lcm, i)
print(lcm)
