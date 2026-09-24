list = [1, 4, 5, -1, 10]

def extract_even(list):
    new_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0 and list[i] > 1:
            new_list.append(list[i])
    return new_list

print(extract_even(list))
