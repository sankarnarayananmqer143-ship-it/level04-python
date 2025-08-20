print("fibonaccoi series")
print("-----------------")
n=int(input("Enter the number:"))
print("fibonacci series")
a=-1
b=1
for i in range(n+1):
    c=b+a
    print(c)
    a=b
    b=c
