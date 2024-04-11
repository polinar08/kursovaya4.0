from abc import ABC, abstractmethod
import requests


class FromAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class FromHHru(FromAPI):
    """Класс для подключения к API и получения списка вакансий"""

    def __init__(self, url_get='https://api.hh.ru/vacancies'):
        self.url_get = url_get

    def get_vacancies(self, keyword):
        """Получает список вакансий в формате json по ключевому слову"""
        response = requests.get(self.url_get, params={'text': keyword, 'area': '113', 'per_page': 100})
        vacancies = response.json()['items']
        return vacancies
