import pandas as pd

def get_star_per_month(business_id):
    '''
    Get star of a shop in each month
    :param business_id: The shop's id
    :returns: Star of the shop every month as a list, the start month and the end month
    '''
    df = pd.read_csv("./new_orlean_restaurant_reviews.csv")
    target_bus_df = df.loc[df['business_id'] == business_id]
    # print("number of reviews: ",len(target_bus_df.index))
    target_bus_df = target_bus_df.sort_values(by=['date'])

    start_year = int(target_bus_df.iloc[0].at['date'][0:4])
    end_year = int(target_bus_df.iloc[-1].at['date'][0:4])
    start_month = int(target_bus_df.iloc[0].at['date'][5:7])
    end_month = int(target_bus_df.iloc[-1].at['date'][5:7])
    stars = []
    for i in range(0,len(target_bus_df.index)):
        stars.append(target_bus_df.iloc[i].at['stars'])

# You can test your function here
def main():
    a_sample_business_id_not_exist = 000000
    print(get_star_per_month(a_sample_business_id_not_exist))

if __name__ == "__main__":
    main()
