print("PRIME NUMBER CHECKING")
print("---------------------")

sn = int(input("Enter the starting number: "))
en = int(input("Enter the ending number: "))

print("Result")
for n in range(sn, en + 1):
    if n < 2:
        print(n, "not prime")
        continue
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
            break
    if count == 0:
        print(n, "prime")
    else:
        print(n, "not prime")
