__author__ = 'Alex Bulavin'
__author__ = 'Alex Bulavin'
import json
import csv
import datetime

# Открытие JSON-файла
with open('recipes.json', 'r') as f:
    data = json.load(f)

# Открытие CSV-файла
with open('recipes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    recipe_number = 1
    # Запись заголовков столбцов
    writer.writerow(['recipe_number', 'id', 'Название', 'Описание',
                     'Энергетическая ценность', 'Время приготовления',
                     'Ингредиенты', 'Количество', 'Размерность'])

    # Запись данных в CSV-файл
    for recipe in data['data']['recipe_description']:
        cooktime_seconds = recipe['cooktime']
        cooktime_minutes, cooktime_seconds = divmod(cooktime_seconds, 60)
        cooktime_hours, cooktime_minutes = divmod(cooktime_minutes, 60)
        cooktime_formatted = datetime.time(hour=cooktime_hours,
                                           minute=cooktime_minutes)\
            .strftime('%H:%M')
        writer.writerow([
                            recipe_number,
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
        recipe_number += 1
