from abc import ABC, abstractmethod
import json


class Methods(ABC):
    """Абстрактный класс для работы с вакансиями"""

    @abstractmethod
    def add_vacancy(self, *args):
        pass

    @abstractmethod
    def get_data(self, *args):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class ListVacancies(Methods):
    """Класс для управления списком вакансий"""

    @staticmethod
    def save_vacancies(vacancies):
        """Записывает список вакансий в файл"""
        with open("../data/vacancies.json", "w", encoding="utf8") as f:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False)
            f.write(vacancies_json)

    def add_vacancy(self, name_vac):
        """Добавляет вакансии в файл по названию"""
        with open("../data/vacancies.json", "r", encoding="utf8") as f:
            list_vacancies = json.load(f)
        with open("../data/my_vacancies.json", "r", encoding="utf8") as f:
            list = json.load(f)
        for v in list_vacancies:
            if name_vac in v["name"]:
                list.append(v)
        list_vacancies_add = json.dumps(list, ensure_ascii=False)
        with open("../data/my_vacancies.json", "w", encoding="utf8") as f:
            f.write(list_vacancies_add)
        return list_vacancies_add

    def get_data(self, criterion):
        """Получает данные из файла по указанному критерию"""
        with open("../data/vacancies.json", "r", encoding="utf8") as f:
            vacancies = json.load(f)
            criterion_vac = []
            for vac in vacancies:
                if criterion in vac["snippet"]["requirement"]:
                    criterion_vac.append(vac)
        return criterion_vac

    def delete_vacancy(self):
        """Удаляет данные о вакансиях из файла"""
        list_vacancies_del = []
        list = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open("../data/my_vacancies.json", "w", encoding="utf8") as f:
            f.write(list)
