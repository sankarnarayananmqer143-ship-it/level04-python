print("SUM OF N NUMBER")
print("---------------")
sn=int(input("Enter the starting number:"))
en=int(input("Enter the ending number:"))
print("Result")
print("------")
print("series")
sum=0
count=0
for i in range(sn,en+1):
    if(i%5==0)and(i%3==0):
        print("+",+i)
sum=sum+i;
count=count+1
print("sum value:",sum)
print("count value:",count)
