n = int(input("Enter: "))
prime = 1

if n <= 1:
    prime = 0
elif n == 2:
    prime = 1
else:
    for i in range(2, n, 1):
        if n % i == 0:
            prime = 0
            
if prime == False:
    print(f"{n} is a NOT prime number")
else:
    print(f"{n} is a prime number")