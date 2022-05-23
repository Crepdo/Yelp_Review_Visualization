import pandas as pd

def get_star_per_month(business_id):
    '''
    Get star of a shop in each month
    :param business_id: The shop's id
    :returns: Star of the shop every month as a list, the start month and the end month
    '''
    data = pd.read_csv("./data/new_orlean_restaurant_reviews.csv")

    # The followings are examples, plz change their values and return
    stars = []
    start_year = 2000
    start_month = 12
    end_year = 2000
    end_month = 12
    return (stars, start_year, start_month, end_year, end_month)


# You can test your function here
def main():
    a_sample_business_id_not_exist = 000000
    print(get_star_per_month(a_sample_business_id_not_exist))

if __name__ == "__main__":
    main()
