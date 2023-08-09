"""1. Програма яка при запуску повинна:
Створити текстовий файл, записати в нього дані, які вводить користувач.
Закінченням введення нехай служить порожній текст.
Кожен введений текст у файлі повинен починатися з нового рядка.
Також треба спитати назву файлу у користувача."""


file_name = input('Enter a name for the file: ')
with open(file_name, 'w') as file:
    while True:
        text = input('Enter your text: ')
        if not text:
            break
        file.write(text + "\n")