from datetime import datetime, date
import calendar
# Функция для запроса даты рождения у пользователя
def get_user_birthday():
    day = int(input("Введите день вашего рождения (1-31): "))
    month = int(input("Введите месяц вашего рождения (1-12): "))
    year = int(input("Введите год вашего рождения: "))
    return date(year, month, day)

# Функция для определения дня недели
def get_weekday(birthday):
    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return weekdays[birthday.weekday()]

# Функция для проверки, является ли год високосным
def is_leap_year(year):
    return calendar.isleap(year)

# Функция для расчета возраста
def calculate_age(birthday):
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

# Функция для вывода даты рождения в формате электронного табло
def print_date_as_stars(day, month, year):
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "    *", " *** ", "*    ", " *** "],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["*   *", "*   *", " *** ", "    *", "    *"],
        '5': [" *** ", "*    ", " *** ", "    *", " *** "],
        '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
        '7': [" *** ", "    *", "    *", "    *", "    *"],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " *** ", "    *", " *** "]
    }
    
    date_str = f"{day:02}{month:02}{year}"
    lines = ["", "", "", "", ""]
    for char in date_str:
        for i in range(5):
            lines[i] += digits[char][i] + "  "
    print("\n".join(lines))

# Основная программа
birthday = get_user_birthday()
weekday = get_weekday(birthday)
leap_year = is_leap_year(birthday.year)
age = calculate_age(birthday)

print("\nДата рождения:", birthday.strftime("%d.%m.%Y"))
print("День недели:", weekday)
print("Високосный год:", "Да" if leap_year else "Нет")
print("Ваш возраст:", age, "лет")

# Вывод даты в формате звездочек
print("\nВаша дата рождения в формате звездочек:")
print_date_as_stars(birthday.day, birthday.month, birthday.year)