a=int(input("enter a number:"))

number_of_digit=len(str(a))
sum_of_digit=0
while a>0 :
   digit=a%10
   sum_of_digit+=digit**number_of_digit
   a /= 10
if a==sum_of_digit:
    print("the number is armstrong")
else:
    print("the number is not armstrong")
