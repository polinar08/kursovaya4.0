from src.API_service import FromHHru
from src.method import VacancyManager
from src.vac_sorting import sorting


def interface():
    """Функция для взаимодействия с пользователем."""
    hh = FromHHru()
    vm = VacancyManager()

    while True:
        user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
        vacancies = hh.get_vacancies(user_vacancy)
        vm.save_vacancies(vacancies)

        name_vac = input('Введите название вакансии для добавления: \n')
        vm.add_vacancy(name_vac)

        name_criterion = input('Введите критерий для отбора вакансий: \n')
        filtered_vacancies = vm.get_data(name_criterion)

        n = input('Введите количество вакансий для просмотра: \n')
        try:
            n = int(n)
            top_vacancies = sorting(filtered_vacancies, n)
            for vac in top_vacancies:
                print(vac)
        except ValueError:
            print("Пожалуйста, введите корректное число.")

        if input('Завершить и очистить файл вакансий? (да/нет): \n').lower() == 'да':
            vm.delete_vacancy()
            break


if __name__ == "__main__":
    interface()
