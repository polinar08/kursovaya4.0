import pytest
import json
from src.API_service import FromHHru
from src.method import ListVacancies


def test_get_vacancies():
    hh = FromHHru()
    result = hh.get_vacancies("Python")
    assert isinstance(result, list), "Ожидался список вакансий"
    assert len(result) > 0, "Список вакансий не должен быть пустым"
    assert 'name' in result[0], "Вакансии должны иметь ключ 'name'"


def test_add_vacancy():
    lv = ListVacancies()
    test_vacancy = "Тестовая вакансия"
    lv.add_vacancy(test_vacancy)

    with open("../data/my_vacancies.json", "r", encoding="utf8") as f:
        list_my_vacancies = json.load(f)
    assert any(vac['name'] == test_vacancy for vac in list_my_vacancies), "Вакансия должна быть добавлена"
