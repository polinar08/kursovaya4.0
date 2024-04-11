import json


def vac_user():
    """Преобразует полученные данные в формат для вывода"""
    with open("../data/vacancies.json", "r", encoding="utf8") as f:
        vacancies = json.load(f)
    user_vac = []
    for vac in vacancies:
        if not vac["salary"]:
            vac["salary"] = 0
        else:
            if vac["salary"]["currency"]:
                vac["currency"] = vac["salary"]["currency"]
            else:
                vac["currency"] = "Валюта не определена"
            if vac["salary"]["from"] is None and vac["salary"]["to"] is None:
                vac["salary"] = 0
            elif vac["salary"]["from"] is None:
                vac["salary"] = vac["salary"]["to"]
            elif vac["salary"]["to"] is None:
                vac["salary"] = vac["salary"]["from"]
            else:
                vac["salary"] = (vac["salary"]["from"] + vac["salary"]["to"]) // 2
        user_vac.append(vac)
    return user_vac
