from utils.headhunter import HeadHunterAPI
from utils.superjob import SuperJobAPI
from utils.JSONsaver import JSONSaver



def user_interaction():

    list_vacansies = []

    filter_vacancy = input('Введите поисковый запрос: ')

    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    hh.get_vacancies(filter_vacancy)
    hh_list = hh.filtered_vacancies()
    sj.get_vacancies(filter_vacancy)
    sj_list = sj.filtered_vacancies()

    jsonsaver = JSONSaver()
    list_vacansies.extend(hh_list)
    list_vacansies.extend(sj_list)
    # print(list_vacansies)
    jsonsaver.save_to_json(list_vacansies)
    list_ = jsonsaver.read_from_file('./data/vacansies.json')

    for item in sorted(list_, reverse=True):
        print(f'{item.name}: {item.salary_from}-{item.salary_to} '
              f'{item.currency.upper() if item.currency != "null" else ""}')


user_interaction()
