print("prime number checting")
print("------------------------")
n=int(input("Enter the number"))
print("result")
count=0
for i in range (2,n):
    if(n%i)==0:
        count=count+1
    if count==0:
      print("is a prime")
    else:
      print("is a not prime")
