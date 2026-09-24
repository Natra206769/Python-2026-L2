m = int(input("Enter the length: "))
n = int(input("Enter the width: "))


def draw(m, n):
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("* " * m)
        else:
            print("*", end=" ")
            print("  " * (m - 2), end="")
            print("*")

draw(m, n)