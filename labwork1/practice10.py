n = int(input("Enter the number: "))

def get_divisors(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    return div

print(get_divisors(n))