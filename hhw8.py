from datetime import datetime, timedelta
from collections import defaultdict
users = [
    {'name': 'Bill', 'birthday': datetime(year=2000,month = 6,day = 7)},
    {'name': 'Jill', 'birthday': datetime(year = 2023,month =  6,day =  7)},
    {'name': 'Kim', 'birthday': datetime(year = 2024,month =  6,day = 5)},
    {'name': 'Jan', 'birthday': datetime(year =2023,month = 6,day= 6)},
]


date = datetime.now().date()
deltadate = timedelta(weeks=1)

def get_birthdays_per_week(users):
    week = date + deltadate
    birth = defaultdict(list)
    for i in users:
        event = datetime(year=week.year,
                         month=i['birthday'].month,
                         day=i['birthday'].day,
                         ).date()
        if date < event <= week:
            if event.weekday() == 5:
                event += timedelta(days=2)
            elif event.weekday() == 6:
                event += timedelta(days=1)
            day = event.strftime('%A:')
            birth[day].append(i['name'])
    for k,v in birth.items():
   
        print(k, ', '.join(v))


get_birthdays_per_week(users)
