a=int(input("enter a number"))

count=0
for number in range(1,a+1):
    if a%number==0:
     count+=1
if count==2:
  print("the number is a prime number")
else:
  print("the number is not a prime")
