print("sum of N number")
print("---------------")
sn=int(input("Enter the strating number:"))
en=int(input("Enter the ending number:"))
df=int(input("different:"))
print("Result")
sum=sn
for i in range(sn,en+1,df):
    print("+",+i)
    sum=sum+i
print("sum value:",sum)
