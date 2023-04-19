# Название файла: dog_life_expectancy.py

breed = input("Введите породу собаки: ")

if breed == "Шпиц":
    life_expectancy = 15
elif breed == "Лабрадор":
    life_expectancy = 12
elif breed == "Джек Рассел терьер":
    life_expectancy = 16
elif breed == "Немецкая овчарка":
    life_expectancy = 10
elif breed == "Чихуахуа":
    life_expectancy = 20
else:
    print("Извините, не знаю среднюю продолжительность жизни для этой породы.")
    exit()

print(f"Средняя продолжительность жизни {breed} составляет примерно {life_expectancy} лет.")
