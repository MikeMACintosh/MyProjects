'''
Отправка запросов по url с отрисовкой времени ответа
'''

import requests
import time
import matplotlib.pyplot as plt

url = input('Введите URL: ')
iter = int(input('Введите количество итераций: '))

def get_avg_time_reauest(url, iter):
    fig, ax = plt.subplots()
    lst1 = []
    lst2 = []
    lst3 = []
    for iteration in range(iter):
        start = time.monotonic()
        r = requests.get(url,timeout=3)
        stop = time.monotonic()
        lst1.append(stop-start)
        print(f'#Итерация', iteration, ':', round(stop-start, 2), 'секунд')
        lst2.append(iteration)
        lst3.append(sum(lst1) / len(lst1))
    print(f'Среднее время ответа:', round(sum(lst1)/len(lst1), 4))
    ax.scatter(lst2, lst1, color='r')
    ax.plot(lst2, lst3)
    plt.xlabel('Итерации')
    plt.ylabel('Время ответа,c')
    plt.show()

if __name__ == '__main__':
    get_avg_time_reauest(url, iter)

