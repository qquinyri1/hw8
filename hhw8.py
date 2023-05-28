from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=7)

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    birthdays_this_week = {}
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()

        if birthday >= start_of_week and birthday < end_of_week:
            if birthday.weekday() >= 5:  
                weekday = weekdays[0]  
            else:
                weekday = weekdays[birthday.weekday()]

            if weekday not in birthdays_this_week:
                birthdays_this_week[weekday] = []
            birthdays_this_week[weekday].append(name)

    if birthdays_this_week:
        print("Список коллег для поздравления на этой неделе:")
        for weekday, names in birthdays_this_week.items():
            names_str = ", ".join(names)
            print(f"{weekday}: {names_str}")
    else:
        print("На этой неделе нет дней рождения.")


users = [
    {'name': 'Александр', 'birthday': datetime(2023, 5, 28)},
    {'name': 'Елена', 'birthday': datetime(2023, 5, 30)},
    {'name': 'Иван', 'birthday': datetime(2023, 6, 2)},
    {'name': 'Мария', 'birthday': datetime(2023, 5, 26)},
    {'name': 'Петр', 'birthday': datetime(2023, 6, 4)},
]

get_birthdays_per_week(users)
