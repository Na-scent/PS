n = int(input())

q = n//3
r = n%3

if (q+r) % 2 == 0:
  print("CY")
else:
  print("SK")
  # dd