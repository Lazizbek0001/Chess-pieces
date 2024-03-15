x1 = int(input("X 1: "))
y1 = int(input("Y 1: "))

x2 = int(input("X 2: "))
y2 = int(input("Y 2: "))

if (x1==x2 or y1==y2) or (abs(x1-x2) == abs(y1-y2)):
  print("You can move")
else:
  print("Sorry You can't move")