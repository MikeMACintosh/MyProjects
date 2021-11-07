from random import choice

# Модуль random не является криптографически стойким, поэтому не рекомендуется
# использовать пароли, полученные с помощью этой программы.

print('\n--------------- Добро пожаловать в генератор паролей ---------------\n')

def Password_gen():
    """
    Функция cлучайным образом генерирует последовательности символов из строки symbols
    и выводит в виде списка заданное колчество паролей заданной длины.
    """
    passwords_lst = []
    symbols = 'qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP[];,0123456789!@#$%^&*()№'

    try:
        password_amount = int(input('Введите количество паролей: '))
        password_length = int(input('Введите длину пароля: '))
    except ValueError:
        raise ValueError('Некорректный ввод')
    assert password_amount > 0 and password_length > 0, 'Введите ненулевое значение'

    for i in range(password_amount):
        password = ''
        for j in range(password_length):
            password += choice(symbols)
        passwords_lst.append(password)
    print(passwords_lst)

if __name__ == '__main__':
    Password_gen()
