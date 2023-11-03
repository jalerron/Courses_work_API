from utils.JSONsaver import JSONSaver, path
from utils.functions import view_vacansies, print_vacansies, make_sort_by_currency


def user_interaction():

    filter_vacancy = input('Введите поисковый запрос: ')
    top_n = input('Введите количество выводимое в топе вакансий по зарплате: ')
    currency = input('Выберите валюту (1-Рубли, 2-Доллары): ')
    platform = input('Выбирите платформу (1-HeadHunter, 2-SuperJOB, 3-обе): ')

    list_vacansies = view_vacansies(platform, filter_vacancy)

    # Создаем экземпляр класса для записи данных в JSON и последующего вывода необходимых вакансий
    jsonsaver = JSONSaver()
    jsonsaver.save_to_json(list_vacansies)

    # Заполнение листа по валюте

    if currency:
        list_ = make_sort_by_currency(currency, jsonsaver.read_from_file(path))
    else:
        list_ = jsonsaver.read_from_file(path)

    if len(list_) == 0:
        print('Нет вакансий по данному запросу.')
    else:
        for item in sorted(list_, reverse=True)[:int(top_n)]:
            print(print_vacansies(item))


if __name__ == "__main__":
    user_interaction()
