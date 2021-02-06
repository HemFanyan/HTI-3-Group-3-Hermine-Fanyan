def stools(number):
    max_height = max(number)

    return sum([max_height - height for height in number])

heights = [int(i) for i in input('Enter heights of students: ').split()]

print(stools(heights))
