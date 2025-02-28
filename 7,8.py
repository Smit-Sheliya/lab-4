n=int(input("enter a value"))
r=int(input("enter a valid value"))
#factorial
#nCr
if r>n:
    print("invalid")
fact_of_n=1
for i in range(1,n+1):
    fact_of_n=fact_of_n*i

print("fact_of_n",fact_of_n)

fact_of_r=1
for j in range(1,r+1):
    fact_of_r=fact_of_r*j

print("fact_of_r",fact_of_r)
x=n-r
fact_of_x=1
for k in range(1,x+1):
    fact_of_x=fact_of_x*k

print("fact_of_x",fact_of_x)
nCr=fact_of_n/(fact_of_r*fact_of_x)
print("nCr",nCr)
#nPr
nPr=nCr*fact_of_r
print("nPr",nPr)
