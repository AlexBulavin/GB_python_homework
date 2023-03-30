__author__ = 'Alex Bulavin'
import json
import datetime
import csv
import requests

# Получаем от пользователя ID устройств
device_ids = input("Введите ID устройств через запятую: ")
device_ids = [int(device_id) for device_id in device_ids.split(",")]

# Определяем параметры запроса
query = """
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
data = {
    "query": query,
    "variables": variables
}

# Отправляем запрос на сервер
url = 'https://cmsql.skydom.company/v1/graphql'
headers = {'Content-type': 'application/json'}
response = requests.post(url, headers=headers,
                         data=json.dumps({'query': query,
                                          'variables': variables}),
                         verify='/path/to/cert.pem')


'''https://cmsql.readyforsky.com/content/devices/'''
# Проверяем успешность запроса
if response.status_code == 200:
    # Преобразуем ответ в csv файл
    """# Открытие JSON-файла
    with open('/Users/alex/Documents/GeekBrains/GB_python_homework/lesson3/recipes.json', 'r') as f:
        data = json.load(f)"""
    data = response.json()["data"]["recipe_description"]

    # Открытие CSV-файла
    with open('file.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        # Запись заголовков столбцов
        writer.writerow(['id', 'Название', 'Описание',
                         'Энергетическая ценность', 'Время приготовления',
                         'Ингредиенты',
                         'Количество', 'Размерность'])

        # Запись данных в CSV-файл
        for recipe in data['data']['recipe_description']:
            cooktime_seconds = recipe['cooktime']
            cooktime_minutes, cooktime_seconds = divmod(cooktime_seconds, 60)
            cooktime_hours, cooktime_minutes = divmod(cooktime_minutes, 60)
            cooktime_formatted = datetime.time(hour=cooktime_hours,
                                               minute=cooktime_minutes)\
                .strftime('%H:%M')
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
