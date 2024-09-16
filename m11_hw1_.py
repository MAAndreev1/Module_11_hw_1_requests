import requests as req
import os
from random import randint


# requests - позволяет отправлять HTTP запросы.  HTTP (HyperText Transfer Protocol, протокол передачи гипертекста)

# В протоколе HTTP описаны различные виды запросов: на получение данных (GET), на передачу данных (POST),
# на добавление и изменение данных (PUT), на удаление данных (DELETE) и др.

try:
    os.remove('./map.png')
except FileNotFoundError:
    pass

coordinates = f'{randint(10, 50) + 0.123456},{randint(10, 50) + 0.123456}'
URL = 'https://static-maps.yandex.ru/1.x/?'
params = {'ll': coordinates, 'spn': '10,10', 'l': 'map', 'pt': f'{coordinates},home'}

response = req.get(URL, params=params)


if response.status_code == 200:
    print(f'Направлен запрос по ссылке: {response.url}')
    print(f'Запрос успешен, ответ получен. Код ответа: {response.status_code}')
    print(f'Время затраченное на запрос: {response.elapsed}')
    with open("map.png", "wb") as file:
        file.write(response.content)
        print(f'Запрос осуществлялся по координатам {coordinates}.')
        print('Фрагмент карты сохранен под именем: "map.png"')
else:
    print(f'Что-то пошло не так! Код ошибки: {response.status_code}')