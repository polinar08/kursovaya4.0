class Vacancy:

    """Класс для работы с вакансиями"""

    def __init__(self, name, salary, currency, url, requirement='Информация отсутствует'):
        self.name = name
        self.salary = salary
        self.currency = currency
        self.url = url
        self.requirement = requirement

    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Зарплата: {self.salary} {self.currency}\n'
                f'Требования: {self.requirement}\n'
                f'Ссылка на вакансию: <{self.url}>\n')

    def __gt__(self, other):

        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""

        if self.salary is not None and other.salary is not None:
            if self.salary['to'] > other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'

    def __lt__(self, other):

        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""

        if self.salary is not None and other.salary is not None:
            if self.salary['to'] < other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'