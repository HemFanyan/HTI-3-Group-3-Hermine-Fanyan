def is_heterogram(word):
    word = word.lower()
    word_count = [word.count(i) for i in word if i != ' ']
    if sum(word_count) == len(word_count):
        return "yes"
    else:
        return 'no'


a = input('Enter a text: ')
print(is_heterogram(a))
