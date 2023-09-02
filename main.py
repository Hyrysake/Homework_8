from datetime import date, datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = date.today()
    current_year = today.year

   
    birthdays_per_week = defaultdict(list)

    if users:
        for user in users:
            name = user['name']
            birthday = user['birthday']
            birthday_this_year = birthday.replace(year=current_year)
            if birthday.month == 1:
                birthday_this_year = birthday.replace(year=current_year + 1)
            else:
                birthday_this_year = birthday.replace(year=current_year)
            if birthday_this_year < today:
                continue


            if birthday_this_year.weekday() >= 5:
             
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            day_name = birthday_this_year.strftime('%A')
            birthdays_per_week[day_name].append(name)
    else:
        return dict()

    return birthdays_per_week





    users = {day: names for day, names in birthdays_per_week.items() }
    return users

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    print(users)

    result = get_birthdays_per_week(users)
    print(result)

    def print_birthdays_per_week(result):
        for day_name, names in result.items():
            print(f"{day_name}: {', '.join(names)}")

    print_birthdays_per_week(result)