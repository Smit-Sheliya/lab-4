a=int(input("enter a number of fibonacci term:"))
x,y=0,1
for _ in range(a):
   print(x,end=" ")
   x, y=y,x+y
