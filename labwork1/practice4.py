n = int(input("Enter: "))
sum = 0

for i in range(1, n, 1):
    if n % i == 0:
        sum += i
        
if n % sum == 0:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")