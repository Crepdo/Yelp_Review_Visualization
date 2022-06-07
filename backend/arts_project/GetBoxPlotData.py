import datetime
import pandas as pd
class PlotData:
    def __init__(self) -> None:
        self.df = pd.read_csv("./resources/new_orlean_restaurant_reviews.csv", parse_dates=['date'])

    def get_box_plot_data(self, business_id):
        result = []
        temp_df = self.df[self.df["business_id"] == business_id]
        print(temp_df["business_id"])
        for index, row in temp_df.iterrows():
            temp_date = row["date"].date()
            temp_date = temp_date.replace(day=1)
            result.append({
                    "date": temp_date.isoformat(),
                    "review_id": row["review_id"],
                    "stars": row["stars"]
                })
        return result

    def get_review_content(self, business_id, review_id):
        temp_df = self.df[self.df["business_id"] == business_id]
        data = temp_df[temp_df["review_id"] == review_id]
        return {
            "text": data["text"],
            "useful": data["useful"],
            "cool": data["cool"]
        }

    def get_positive_highest(self, business_id, start_date, end_date):
        temp_df = self.df[self.df["business_id"] == business_id]
        datas = temp_df[(temp_df["date"] > start_date) & (temp_df["date"] < end_date)]
        data = temp_df[temp_df["useful"] == temp_df.loc[:, "useful"].max()]
        return self.get_review_content(data.iloc[0]["review_id"])
