from utils.headhunter import HeadHunterAPI
from utils.superjob import SuperJobAPI


def view_vacansies(platform, filter_vacancy):
    """
    Вывод вакансий по платформе
    :param platfom: 1-HH, 2-SJ, 3-Обе
    :param filter_vacancy: Вакансии по ключевому слову
    :return: list_vacansies
    """
    if platform == "1":
        # Создаем экземпляры классов API
        hh = HeadHunterAPI()
        # Получаем вакансии согласно запросу
        hh.get_vacancies(filter_vacancy)
        # Формируем списки вакансий с отформатированными полями
        hh_list = hh.filtered_vacancies()

        return hh_list

    elif platform == "2":
        # Создаем экземпляры классов API
        sj = SuperJobAPI()
        # Получаем вакансии согласно запросу
        sj.get_vacancies(filter_vacancy)
        # Формируем списки вакансий с отформатированными полями
        sj_list = sj.filtered_vacancies()

        return sj_list

    elif platform == "3":

        list_both = []
        # Создаем экземпляры классов API
        hh = HeadHunterAPI()
        sj = SuperJobAPI()
        # Получаем вакансии согласно запросу
        sj.get_vacancies(filter_vacancy)
        hh.get_vacancies(filter_vacancy)
        # Формируем списки вакансий с отформатированными полями
        list_both.extend(hh.filtered_vacancies())
        list_both.extend(sj.filtered_vacancies())

        return list_both

    else:
        raise Exception('Выбрана неверная платформа')


def make_sort_by_currency(currency, list):
    list_ = []
    if currency == "1":
        for item in list:
            if item.currency.upper() == "RUB" or "RUR":
                list_.append(item)
    elif currency == "2":
        for item in list:
            if item.currency.upper() == "USD":
                list_.append(item)

    return list_


def print_vacansies(item):
    return f'\n{item.name}:\n'\
           f'{item.salary_from}-{item.salary_to}  {item.currency.upper() if item.currency != "null" else ""}\n'\
           f'{item.area}\n{item.requirement}\n{item.url}\n\n'
