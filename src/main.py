from ast import main

from src.API_service import FromHHru
from src.method import ListVacancies
from src.vac_sorting import sorting


def interface():
    """Функция для взаимодействия с пользователем"""
    while True:
        user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
        hh = FromHHru()
        vacancies = hh.get_vacancies(user_vacancy)

        fv = ListVacancies()
        fv.save_vacancies(vacancies)

        name_vac = input('Введите название вакансии для добавления: \n')
        fv.add_vacancy(name_vac)

        name_criterion = input('Введите критерий для отбора вакансий: \n')
        filtered_vacancies = fv.get_data(name_criterion)

        n = input('Введите количество вакансий для просмотра: \n')
        try:
            top_vacancies = sorting(filtered_vacancies, int(n))
            for vac in top_vacancies:
                print(vac)
        except ValueError:
            print("Пожалуйста, введите корректное число.")

        name_exit = input('Завершить и очистить файл вакансий? (да/нет): \n')
        if name_exit.lower() == 'да':
            fv.delete_vacancy()
            break


if __name__ == "__main__":
    main()
