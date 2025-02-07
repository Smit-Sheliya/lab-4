a=int(input("enter a number"))
count=0
for number in range(1,a):
    if a%number==0:
     count+=number
if a==count:
   print("the number is perfect")
else:

   print("the number is not perfect")
