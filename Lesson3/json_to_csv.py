__author__ = 'Alex Bulavin'
import json
import csv
import datetime

# Открытие JSON-файла
with open('/Users/alex/Documents/GeekBrains/GB_python_homework/lesson3/recipes.json', 'r') as f:
    data = json.load(f)

# Открытие CSV-файла
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Запись заголовков столбцов
    writer.writerow(['id', 'Название', 'Описание', 'Энергетическая ценность', 'Время приготовления', 'Ингредиенты',
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
                            recipe['recipe']['translatable_fields'][0]['name'],
                            recipe['translatable_fields'][0]['description'],
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
                ingredient['quantity_unit']['translatable_fields'][0]['name']
            ])
