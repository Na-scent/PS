import sys
while True:
  a, b, c = map(int, input().split())
  if a == b and b == c:
      if a ==0:
        sys.exit()
      else:
        print("Equilateral")
  elif (a+b+c) - 2*max(a, b, c) <= 0:
    print("Invalid")
  else:
    if a != b and b != c and a != c:
      print("Scalene")
    else:
      print("Isosceles")