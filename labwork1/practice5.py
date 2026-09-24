colors = ["red", "yellow", "orange"]
prompt = input("Enter your favorite color: ")

for i in range(0, len(colors)):
    if prompt == colors[i]:
        print(f"Your color is at index {i} in my list")
        break
    else:
        print("Sorry, I could not find your color")