import requests

tmp_list = []
n = int(input())
for i in range(n):
    i = int(input())
    tmp_list.append(i)
print(tmp_list)

params = {
    'number': tmp_list,
    'type': 'math',
    'json': 'true'
    }

def ParseNumber():
    """
    Функция отправляет запрос по адресу 'http://numbersapi.com' и выдает ответ по каждому числу,
    введённому пользователем, "интересное" оно, или "скучное".
    """
    for i in tmp_list:
        res = requests.get(f'http://numbersapi.com/{i}/math?json=true')
        data = res.json()
        if data['found'] == True:
            print('Interesting')
        else:
            print('Boring')

if __name__ == '__main__':
    ParseNumber()


