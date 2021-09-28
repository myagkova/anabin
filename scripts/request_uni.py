import requests
import json
import csv


URL = "https://anabin.kmk.org/no_cache/filter/institutionen.html"
eID = "user_anabin_institutionen"
conf = "institutionsergebnisliste"
sSearch_6 = "Russische+F%C3%B6deration"
land = "30"

PARAMS = {"eID":eID, "conf":conf, "sSearch_6":sSearch_6, "land":land}


def main():
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)
    # with open('data.json') as f:
    #     data = json.load(f)

    for university in data['aaData']:
        uni_id = university[1]
        name = university[2]
        city = university[3]
        accreditation = university[5]
        print(uni_id, name, city, accreditation, sep=", ")

    # print(data)


if __name__ == "__main__":
    main()
