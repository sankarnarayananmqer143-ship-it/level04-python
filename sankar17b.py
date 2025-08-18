print("sum of N number")
print("---------------")
sn=int(input("Enter the starting number:"))
en=int(input("Enter the ending number:"))
print("Result")
sum=sn
for i in range(sn,en+1):
    print("+",+i)
    sum=sum+i
print("sum value is:",sum)
