print("Prime Number Generation")
print("------------------------")

sn = int(input("Enter the starting number: "))
en = int(input("Enter the ending number: "))

print("Result:")

for n in range(sn, en):
    if n < 2:
        print(n, "not prime")
        continue
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
            break  # No need to keep checking if a divisor is found
    if count == 0:
        print(n, "prime")
    else:
        print(n, "not prime")
