__author__ = 'Alex Bulavin'

import json
import os
import ssl
import datetime
import csv
import requests
import sys

sys.path.append('/Users/alex/Documents/Secutity/')
from Секьюрити.p12_pass import password
from query import query

# Получаем от пользователя ID устройств
device_ids = input("Введите ID устройств через запятую: ")
device_ids = [int(device_id) for device_id in device_ids.split(",")]

# Определяем параметры запроса
graphql_query = """
query getRecipes($deviceIds: [Int!], $categoryId: Int, $descriptionIds: [Int!], $locale: String!, $recipeId: Int, $query: String, $offset: Int, $limit: Int) {
  recipe_description(
    distinct_on: [recipe_id]
    where: {
      devices: {device_id: {_in: $deviceIds}},
      id: {_in: $descriptionIds},
      recipe: {
        id: {_eq: $recipeId}
        recipe_tags: {tag_id: {_eq: $categoryId}}
        translatable_fields: {
          name: {_ilike: $query},
        }
      },
      translatable_fields: {
        locale: {_eq: $locale}
      }
    },
    limit: $limit,
    offset: $offset
  ) {
    id
    state
    energy
    cooktime
    translatable_fields(where: {locale: {_eq: $locale}}) {
      description
    }
    recipe {
      id
      state
      image_id
      translatable_fields(where: {locale: {_eq: $locale}}) {
        name
      }
    }
    recipe_ingredients {
            id
            state
            quantity
            quantity_unit {
                id
                type
                multiplier
                translatable_fields(where: {locale: {_eq: $locale}}) {
                    name
                }
            }
            ingredient {
                id
                state
                translatable_fields(where: {locale: {_eq: $locale}}) {
                    name
                }
            }
        }
    recipe_steps {
      id
      time
      temperature
      program
      tools {
        id
        time
        tool {
          id
          translatable_fields(where: {locale: {_eq: $locale}}) {
            name
          }
          image_id
        }
      }
    }
  }
}
"""
query_params = {
    "device_id": device_ids,  # 16229,
    "order_by_created_at": False,
    "order_by_view_count": True,
    "limit": 10,
    "locale": "ru",
    "offset": 0
    # "deviceIds": device_ids,
    # "categoryId": None,
    # "descriptionIds": None,
    # "locale": "ru_RU",
    # "recipeId": None,
    # "query": None,
    # "offset": 0,
    # "limit": 100
}
variables = {
    "deviceIds": device_ids,
    "categoryId": None,
    "descriptionIds": None,
    "locale": "ru_RU",
    "recipeId": None,
    "query": None,
    "offset": 0,
    "limit": 100
}
# data = {
#     "query": query,
#     "variables": variables
# }

# Создайте объект сессии
session = requests.Session()
p12_path = '/Users/alex/Downloads/client (5).p12'
p12_password = password
key_file = "/Users/alex/Documents/Secutity/Секьюрити/p12_pass.py"
if not os.path.exists(key_file):
    print(f'Error: Could not find the TLS key file at {key_file}')
else:
    print(f'TLS key file at {key_file} found')

# Загрузите p12-сертификат в объект сессии
session.cert = (p12_path, key_file)

# Отправляем запрос на сервер
url = 'https://content.dev.skydom.company/v1/graphql'  # 'https://cmsql.skydom.company/v1/graphql'
headers = {'Content-type': 'application/json'}
response = requests.post(url, headers=headers,
                         data=json.dumps({'query': query,
                                          'variables': variables}))
print(f'requests.post at line 125 passed')
# Отправьте запрос на сервер
# response1 = session.post(url, json={'query': graphql_query, 'variables': query_params})
# print(f'line 131 response1.status_code = {response1.status_code}')
# '''https://cmsql.readyforsky.com/content/devices/'''
# Проверяем успешность запроса
print(f'line 134 response.status_code = {response.status_code}')
if response.status_code == 200:
    # Преобразуем ответ в csv файл
    """# Открытие JSON-файла
    with open('/Users/alex/Documents/GeekBrains/GB_python_homework/lesson3/recipes.json', 'r') as f:
        data = json.load(f)"""
    print(f'line 146 response.json() = {response.json()["data"]["recipe_description"]}')
    data = response.json()["data"]  # ["recipe_description"]

    # Открытие CSV-файла
    with open('file.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        # Запись заголовков столбцов
        writer.writerow(['id', 'Название', 'Описание',
                         'Энергетическая ценность', 'Время приготовления',
                         'Ингредиенты',
                         'Количество', 'Размерность'])

        # Запись данных в CSV-файл
        for recipe in data['recipe_description']:  # data['data']['recipe_description']:
            cooktime_seconds = recipe['cooktime']
            cooktime_minutes, cooktime_seconds = divmod(cooktime_seconds, 60)
            cooktime_hours, cooktime_minutes = divmod(cooktime_minutes, 60)
            cooktime_formatted = datetime.time(hour=cooktime_hours,
                                               minute=cooktime_minutes) \
                .strftime('%H:%M')
            print(f'line178',
                  recipe['id'],
                  recipe['recipe']['translatable_fields'][0]
                  ['name'],
                  recipe['translatable_fields'][0]
                  ['description'],
                  recipe['energy'],
                  cooktime_formatted, "", "", "")
            writer.writerow([
                recipe['id'],
                recipe['recipe']['translatable_fields'][0]
                ['name'],
                recipe['translatable_fields'][0]
                ['description'],
                recipe['energy'],
                cooktime_formatted, "", "", ""])
            for ingredient in recipe['recipe_ingredients']:
                if ingredient['quantity'] == 0:
                    text = "По вкусу"
                else:
                    text = ingredient['quantity']
                writer.writerow([
                    "", "", "", "", "",
                    ingredient['ingredient']['translatable_fields'][0]['name'],
                    text,
                    ingredient['quantity_unit']['translatable_fields'][0]
                    ['name']
                ])
