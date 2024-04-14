from abc import ABC, abstractmethod
import json
import os


class AbstractVacancyManager(ABC):
    """Абстрактный класс для управления вакансиями."""

    @abstractmethod
    def add_vacancy(self, name_vac: str):
        pass

    @abstractmethod
    def get_data(self, criterion: str):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class VacancyManager(AbstractVacancyManager):
    """Класс для управления списком вакансий."""

    def __init__(self):
        # Пути к файлам данных
        self.data_file = "../data/vacancies.json"
        self.my_vacancies_file = "../data/my_vacancies.json"

    @staticmethod
    def save_vacancies(vacancies: list):
        """Сохраняет список вакансий в файл."""
        with open("../data/vacancies.json", "w", encoding="utf8") as f:
            json.dump(vacancies, f, ensure_ascii=False)

    def add_vacancy(self, name_vac: str) -> list:
        """Добавляет вакансии в файл на основе имени."""
        # Проверка и инициализация файла my_vacancies.json, если он пуст или не существует
        if not os.path.exists(self.my_vacancies_file) or os.path.getsize(self.my_vacancies_file) == 0:
            with open(self.my_vacancies_file, "w", encoding="utf8") as f:
                json.dump([], f)

        with open(self.data_file, "r", encoding="utf8") as f:
            list_vacancies = json.load(f)

        with open(self.my_vacancies_file, "r", encoding="utf8") as f:
            list_my_vacancies = json.load(f)

        for v in list_vacancies:
            if name_vac in v["name"]:
                list_my_vacancies.append(v)

        with open(self.my_vacancies_file, "w", encoding="utf8") as f:
            json.dump(list_my_vacancies, f, ensure_ascii=False)
        return list_my_vacancies

    def get_data(self, criterion: str) -> list:
        """Получает данные из файла на основе указанного критерия."""
        with open(self.data_file, "r", encoding="utf8") as f:
            vacancies = json.load(f)
        return [vac for vac in vacancies if criterion in vac["snippet"]["requirement"]]

    def delete_vacancy(self):
        """Удаляет все сохраненные вакансии."""
        with open(self.my_vacancies_file, "w", encoding="utf8") as f:
            json.dump([], f)