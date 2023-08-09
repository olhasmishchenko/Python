"""Написати функцію яка поверне найдовше слово
у рядку: longest_word("What makes a good man") -> makes"""


def find_longest_word(text: str):
    longest_word = max(text, key=len)
    return print(longest_word)


user_text = input('Please enter a few words: ')
word = user_text.split()
print(find_longest_word(word))

