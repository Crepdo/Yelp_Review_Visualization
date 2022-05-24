import random
import datetime
from dateutil.relativedelta import relativedelta

def get_star_per_month(business_id):
    start_year = random.randint(2010, 2019)
    end_year = random.randint(start_year + 1, 2021)
    start_month= random.randint(0, 12)
    end_month= random.randint(0, 12)

    month_count = (end_year - start_year) * 12 + (end_month - start_month) + 1

    stars = []
    for i in range(month_count):
        stars.append(random.random() * 5)

    return (stars, start_year, start_month, end_year, end_month)

def get_star_per_month_json(business_id):
    (stars, start_year, start_month, end_year, end_month) = get_star_per_month(business_id)
    start_data = datetime.date(start_year, start_month, 1)
    end_data = datetime.date(end_year, end_month, 1)
    cur_data = start_data
    result = []
    i = 0
    while cur_data <= end_data:
        result.append({
            "month": cur_data.isoformat(),
            "star": stars[i]
            })
        i += 1
        cur_data += relativedelta(months=1)

    return result
