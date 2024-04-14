import json


def vac_user():
    """Преобразует полученные данные в формат для вывода."""
    with open("../data/vacancies.json", "r", encoding="utf8") as f:
        vacancies = json.load(f)

    processed_vacancies = []
    for vac in vacancies:
        salary_info = vac.get("salary", {}) or {}
        currency = salary_info.get("currency", "Валюта не определена")

        salary_from = salary_info.get("from")
        salary_to = salary_info.get("to")

        salary = 0
        if salary_from and salary_to:
            salary = (salary_from + salary_to) // 2
        elif salary_from:
            salary = salary_from
        elif salary_to:
            salary = salary_to

        processed_vac = {
            'name': vac.get('name'),
            'salary': salary,
            'currency': currency,
            'url': vac.get('alternate_url', 'URL не предоставлен'),
            'requirement': vac.get("snippet", {}).get('requirement', 'Требования не указаны')
        }
        processed_vacancies.append(processed_vac)

    return processed_vacancies
