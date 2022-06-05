import datetime
from dateutil.relativedelta import relativedelta
import random


def get_words_stream_data(business_id):

    person_phrase = "1 2 3 4 5 6 7 8 9"
    person_phrase = person_phrase.split()
    person_phrase = list(set(person_phrase))

    env_phrase = "How to Randomly Select Element From List in Python"
    env_phrase = env_phrase.split()
    env_phrase = list(set(env_phrase))

    start_year = random.randint(2010, 2019)
    end_year = random.randint(start_year + 1, 2021)
    start_month= random.randint(1, 12)
    end_month= random.randint(1, 12)

    print("start_month: ", start_month)
    print("end_month: ", end_month)

    start_date = datetime.date(start_year, start_month, 1)
    end_date = datetime.date(end_year, end_month, 1)
    cur_date = start_date
    result = []
    while cur_date <= end_date:
        print(cur_date)
        cur_data = {}
        cur_data["date"] =  str(cur_date.month) + " " + str(cur_date.year) 
        cur_data["words"] = {}
        cur_person_words = []
        for word in person_phrase:
            cur_person_words.append({
                "sudden": random.randint(3, 6),
                "text": word,
                "frequency": random.randint(2, 5),
                "topic": "person",
                "id": word + "_id"
                })
        cur_env_words = []
        for word in env_phrase:
            cur_env_words.append({
                "sudden": random.randint(3, 6),
                "text": word,
                "frequency": random.randint(2, 5),
                "topic": "environment",
                "id": word + "_id"
                })

        cur_data["words"]["person"] = cur_person_words
        cur_data["words"]["environment"] = cur_env_words
        result.append(cur_data)

        cur_date += relativedelta(months=1)

    return result

if __name__ == "__main__":
    print(get_words_stream_data(0))
