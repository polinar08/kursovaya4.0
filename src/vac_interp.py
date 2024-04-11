import json


def vac_user():

    """Приводим полученные данные к данным для вывода"""

    with open("../data/vacancies.json", "r", encoding="utf8") as f:
        vacancies = json.load(f)
    user_vac = []
    for vac in vacancies:
        if not vac["salary"]:
            vac["salary"] = 0
        else:
            if vac["salary"] is None:
                vac["salary"] = 0
            else:
                if vac["salary"]["currency"]:
                    vac["currency"] = vac["salary"]["currency"]
                else:
                    vac["currency"] = "Валюта не определена"
                if vac["salary"]["from"] is None and vac["salary"]["to"] is None:
                    vac["salary"] = 0
                else:
                    if vac["salary"]["from"] is None and vac["salary"]["to"] is not None:
                        vac["salary"] = vac["salary"]["to"]
                    else:
                        if vac["salary"]["from"] is not None and vac["salary"]["to"] is None:
                            vac["salary"] = vac["salary"]["from"]
                        else:
                            if vac["salary"]["from"] is not None and vac["salary"]["to"] is not None:
                                vac["salary"] = vac["salary"]["to"]

        if vac["snippet"]["requirement"]:
            vac["snippet"]["requirement"] = vac["snippet"]["requirement"]
        else:
            vac["snippet"]["requirement"] = "Информация отсутствует"
        user_vac.append(vac)
    return user_vac