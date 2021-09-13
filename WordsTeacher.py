'''
Программа для изучения слов английского языка - 'Words Teacher'
Пользователь вводит уровень сложности, на котором он будет тренироваться, и количество слов.
Программа выдает слово, пользователь пишет перевод этого слова, если ответ верный - пользователю добавляется балл,
если нет - снимается, далее переход к следующему слову, если их количество больше одного.

Слова хранятся в словаре, где ключем является слово на английском языке, а значение - его перевод на русском языке.
'''

from random import choice
import sys

Beginner = {
    'Mother': ['Мама', 'Мать'],
    'Father': 'Папа'
    }
Intermediate = {
    'Beautiful': 'Прекрасный',
    'Continuous': 'Непрерывный',
    'Garden': 'Сад',
    }
Advanced = {
    'Congratulations': 'Поздравляю',
    'Establishment': 'Учреждение'
    }

def users_choice():
    while True:
        level = int(input("Enter the desired difficulty level (number): (1)Beginner,(2)Intermediate,(3)Advanced: "))
        if level not in [1, 2, 3]:
            print('\n\tDifficulty entered incorrectly, please try again!\n')
        else:
            break

    if level == 1:
        level = Beginner
    elif level == 2:
        level = Intermediate
    elif level == 3:
        level = Advanced

    while True:
        number = input('Enter the quantity of words: ')
        if str(number).isdigit():
            number = int(number)
            break
        else:
            print('\n\tWrong word count, please try again!\n')

    if number > len(level):
        number = len(level)

    for i in range(number):
        Total = 0
        word = choice(list(level))
        print('Enter word translation', word, ':')
        user_input = input()
        if not str(user_input).istitle():
            user_input = str(user_input).title()
        if user_input in level[word]:
            Total += 1
            print('Right! Your result:', Total)
        else:
            Total -= 1
            print('Wrong, please try again! Your result:', Total)

while True:
    users_choice()
    while True:
        print('\n--Do you want to continue? [Y/N]--\n')
        user = input()
        if user not in ['y', 'n', 'Y', 'N']:
            print('\n--Invalid entry, please try again--\n')
        elif user in ['Y', 'y']:
            break
        elif user in ['N', 'n']:
            raise SystemExit('GoodBye! Welcome back soon!')






