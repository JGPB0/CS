import sys 
from libnum import ecc

# y^2 = x^3 + ax + b (mod p)
a = 5
b = 7
p = 97

if len(sys.argv) > 1:
  a = int(sys.argv[1])
if len(sys.argv) > 2:
  b = int(sys.argv[2])
if len(sys.argv[3]):
  p = int(sys.argv[3])

c = ecc.Curve(a, b, p)
print("y^2 = x^3 + %dx+%d (mod %d)\n" % (a, b, p)) 

if p < 100:
  print(c.find_points_in_range(1, p-1))
else:
  print(c.find_points_in_range(1, 100))
