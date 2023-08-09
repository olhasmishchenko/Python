"""Написати функцію яка частково приховуватиме e-mail,
 приклад: hide_email(somebody_email@gmail.com) -> em***@**il.com"""


def hide_email(email: str):
    user, dom_name = email.split("@")
    if len(user) > 2:
        user_secret_name = f'{user[:2]}***'
    else:
        user_secret_name = f'{user[0]}***'
    dom_secret = f'**{dom_name[3:]}'
    return print(f'{user_secret_name}@{dom_secret}')


i = 's@gmail.com'
print(hide_email(i))