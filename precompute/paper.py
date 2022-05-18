import CONSTANT
import json

def read_file(file_path:str, filter_fun, attr:str=""):
    with open(file_path) as f:
        for line in f:
            if(attr==""):
                yield json.loads(line)
            else:
                if(filter_fun(json.loads(line))):
                    yield json.loads(line)[attr]
            

if __name__ == '__main__':
    for k in read_file(CONSTANT.MAIN_DATASET_PATH, lambda x: x["city"] == "Charlotte", "business_id"):
        print(k)

