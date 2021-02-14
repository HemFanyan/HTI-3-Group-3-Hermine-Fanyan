def is_palindrome(text):
    if len(text) < 2:
         return True

    if text[0] != text[-1]:
         return False

    return is_palindrome(text[1:-1])

text = input('Enter a text for palindrome check: ')

if is_palindrome(text):
    print('Yes')
else:
    print('No')
