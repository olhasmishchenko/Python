"""Написати функцію, яка визначить, чи є введений текст
паліндромом (той який читається однаково з будь-якого боку),
приклад:"""


def is_palindrome(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    else:
        return False


print(is_palindrome("ТЕНЕТ"))
print(is_palindrome("Алгоритм"))