from datetime import datetime



def get_days_from_today(date):
    date = datetime.strptime(date, "%Y.%m.%d").date()
    date_now = datetime.now().date()
    days_difference = date_now - date
    return days_difference


print(get_days_from_today('2024.02.22'))



