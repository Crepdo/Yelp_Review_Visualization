import datetime
from dateutil.relativedelta import relativedelta
import random

def get_words_stream_data(business_id):
    person_phrase = [
        "'oyster' 'fry' 'order' 'time' 'take' 'gumbo' 'good' 'cold' 'well' 'food'",
        "'make' 'place' 'bread' 'definitely' 'food' 'drink" 'excellent' 'SSflavor', 
        "'bread' 'try' 'lobster' 'shrimp' 'small' 'gumbo' 'good' 'flavor' 'well' 'chargrille'",
        "'oyster' 'juicy' 'plenty' 'time' 'take' 'gumbo' 'menu' 'place' 'well' 'food'",
        "'oyster' 'juicy' 'order' 'cream' 'take' 'gumbo' 'catfish' 'style' 'well' 'pasta'",
        "'oyster' 'deep' 'dinner' 'ice' 'take' 'drink' 'drago' 'style' 'seafood' 'pasta'"
    ]
    for i in range(0,len(person_phrase)):
        mid = person_phrase[i].split()
        person_phrase[i] = list(set(mid))

    env_phrase = [
        "'service' 'park' 'cold' 'entree' 'gator' 'come' 'place' 'make' 'charbroile'",
        "'service' 'park' 'gator' 'sirloin' 'plenty' 'card' 'place' 'make' 'park'",
        "'service' 'mark' 'get' 'like' 'excellent' 'card' 'place' 'ring' 'charbroile'"
        "'order' 'park' 'cold' 'entree' 'excellent' 'seat' 'order' 'make' 'charbroile'",
        "'service' 'park' 'friend' 'like' 'bread' 'card' 'place' 'make' 'charbroile'",
        "'service' 'mark' 'get' 'like' 'excellent' 'park' 'place' 'ring' 'meet'"
    ]
    for i in range(0,len(env_phrase)):
        mid = env_phrase[i].split()
        env_phrase[i] = list(set(mid))

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
        for word in person_phrase[random.randint(0, 4)]:
            cur_person_words.append({
                "sudden": random.randint(3, 6),
                "text": word,
                "frequency": random.randint(2, 5),
                "topic": "Food",
                "id": word + "_id"
                })
        cur_env_words = []
        for word in env_phrase[random.randint(0, 4)]:
            cur_env_words.append({
                "sudden": random.randint(3, 6),
                "text": word,
                "frequency": random.randint(2, 4),
                "topic": "Environment",
                "id": word + "_id"
                })

        cur_data["words"]["Food"] = cur_person_words
        cur_data["words"]["Environment"] = cur_env_words
        result.append(cur_data)

        cur_date += relativedelta(months=1)

    return result

if __name__ == "__main__":
    print(get_words_stream_data(0))
