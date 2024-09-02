#2. Python program to display powers of 2 using anonymous function.

n = int(input("Enter a number: "))
print("The total power of 2's from 0 to {} is ".format(n))
result=list(map(lambda i:2**i,range(n+1)))
#in abouve line lambda function(anonymous function) iterate 0 to n+1 and map after the convert it into list 
for i in range(n+1):
    print("2 raised to the power of",i,"is",result[i])