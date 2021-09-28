import requests
import json
import csv


URL = "https://anabin.kmk.org/no_cache/filter/hochschulabschluesse.html"
eID = "user_anabin_abschluesse"
conf = "abschlussergebnisliste"
sSearch_8 = "Russische+F%C3%B6deration"
land = "30"

PARAMS = {"eID":eID, "conf":conf, "sSearch_8":sSearch_8, "land":land}


def main():
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)
    # with open('data.json') as f:
    #     data = json.load(f)

    for specialisation in data['aaData']:
        special_id = specialisation[1]
        name_full = specialisation[2]
        degree = specialisation[3]
        duration_min = specialisation[4]
        duration_max = specialisation[5]
        field = specialisation[7]
        print(special_id, name_full, degree, duration_min, duration_max, field,
              sep=", ")

    # print(data)


if __name__ == "__main__":
    main()