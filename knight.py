x1 = int(input("X 1: "))
y1 = int(input("Y 1: "))

x2 = int(input("X 2: "))
y2 = int(input("Y 2: "))

if (abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==2):
  print("You can move")
else:
  print("Sorry you can't move")