from abc import ABC, abstractmethod
import json


class Methods(ABC):

    """Абстрактный класс"""

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

    @staticmethod
    def save_vacancies(vacancies):

        """Запись списка вакансий в файл"""

        with open("../data/vacancies.json", "w", encoding="utf8") as f:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False)
            f.write(vacancies_json)

    def add_vacancy(self, name_vac):

        """Метод для добавления вакансий в файл"""

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

        """Метод получения данных из файла по указанным критериям"""

        with open("../data/vacancies.json", "r", encoding="utf8") as f:
            vacancies = json.load(f)
            criterion_vac = []
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac

    def delete_vacancy(self):

        """Метод удаления данных из файла"""

        list_vacancies_del = []
        list = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open("../data/my_vacancies.json", "w", encoding="utf8") as f:
            f.write(list)