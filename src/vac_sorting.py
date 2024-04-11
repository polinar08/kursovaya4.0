from src.vacancy import Vacancy
from src.translation import vac_user

user_vac = vac_user()


def sorting(n):

    """Сортируем и получаем запрошенное количество вакансий для вывода по зарплате"""

    sorted_list = sorted(user_vac, key=lambda x: x['salary'], reverse=True)
    sorted_vac = sorted_list[:n]
    sort_vac = []
    for vac in sorted_vac:
        if not vac["salary"]:
            vac["salary"] = 0
        else:
            if vac["salary"] is None:
                vac["salary"] = 0
        sort_vac.append(Vacancy(vac['name'], vac['salary'], vac['currency'], vac['url'], vac["snippet"]['requirement']))
    print(sort_vac)
    return sort_vac