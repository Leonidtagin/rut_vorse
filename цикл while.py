my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
while number < len(my_list):
    number += 1
    continue
    if my_list[number] == 0:
        break
    print(my_list[number])
    number += 1