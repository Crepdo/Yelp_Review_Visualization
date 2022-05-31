import random
import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta

def get_star_per_month(business_id):
    df = pd.read_csv("./resources/new_orlean_restaurant_reviews.csv")
    target_bus_df = df.loc[df['business_id'] == business_id]
    target_bus_df = target_bus_df.sort_values(by=['date'])

    start_year = int(target_bus_df.iloc[0].at['date'][0:4])
    end_year = int(target_bus_df.iloc[-1].at['date'][0:4])
    start_month = int(target_bus_df.iloc[0].at['date'][5:7])
    end_month = int(target_bus_df.iloc[-1].at['date'][5:7])
    # star - month dictionary re-scaled to 0 - (month_count-1)
    star_month_dict = {}
    for i in range(0,len(target_bus_df.index)):
        real_year = int(target_bus_df.iloc[i].at['date'][0:4])
        real_month = int(target_bus_df.iloc[i].at['date'][5:7])
        key_month = (real_year - start_year) * 12 + (real_month - start_month)
        if key_month in star_month_dict:
            star_month_dict[key_month].append(target_bus_df.iloc[i].at['stars'])
        else:
            star_month_dict[key_month] = [target_bus_df.iloc[i].at['stars']]
    # ensure every month has a average star
    month_count = (end_year - start_year) * 12 + (end_month - start_month) + 1
    per_month_stars = []
    for key_month in range(month_count):
        if key_month in star_month_dict:
            per_month_stars.append(sum(star_month_dict[key_month])/len(star_month_dict[key_month]))
        else:
            per_month_stars.append(per_month_stars[key_month-1])
    return (per_month_stars, start_year, start_month, end_year, end_month)

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
