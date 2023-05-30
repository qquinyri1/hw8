import datetime

def get_birthdays_per_week(users):
    today = datetime.date.today()
    current_weekday = today.weekday() 

   
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

   
    weekdays = weekdays[current_weekday:] + weekdays[:current_weekday]

   
    birthdays_per_week = {weekday: [] for weekday in weekdays}

    
    for user in users:
        birthday = user['birthday']
        if birthday.weekday() in [5, 6]: 
           
            monday = today + datetime.timedelta(days=(7 - current_weekday))
            birthdays_per_week[weekdays[0]].append(user['name'])
        else:
           
            birthday_weekday = weekdays[birthday.weekday()]
            birthdays_per_week[birthday_weekday].append(user['name'])

   
    for weekday, names in birthdays_per_week.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")


users = [
    {'name': 'Bill', 'birthday': datetime.date(2000, 5, 30)},
    {'name': 'Jill', 'birthday': datetime.date(2023, 5, 31)},
    {'name': 'Kim', 'birthday': datetime.date(2024, 6, 2)},
    {'name': 'Jan', 'birthday': datetime.date(2023, 6, 2)},
]

get_birthdays_per_week(users)
