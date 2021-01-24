t_number = list(input('Enter pair digit number: '))
new_list = [int(i) for i in t_number]
f_half = int(len(new_list)/2)
if len(t_number) % 2 == 0:
    if sum(new_list[:first_half]) == sum(new_list[f_half:]):
        print("Yes")
    else:
        print("No")