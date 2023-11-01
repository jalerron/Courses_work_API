from utils.headhunter import HeadHunterAPI
from utils.superjob import SuperJobAPI
from utils.vacancy import Vacancy
from utils.JSONsaver import JSONSaver
import json
from utils.abstract import abstract_api


# Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
# superjob_api = SuperJobAPI()
#
# # Получение вакансий с разных платформ
# hh_vacancies = hh_api.get_vacancies("Python")
# superjob_vacancies = superjob_api.get_vacancies("Python")

# Создание экземпляра класса для работы с вакансиями
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)

# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter", "SuperJob"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

#     if not filtered_vacancies:
#         print("Нет вакансий, соответствующих заданным критериям.")
#         return

#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)

def user_interaction():
    filter_vacancy = input('Введите поисковый запрос: ')

    hh = HeadHunterAPI()
    data = json.loads(hh.get_vacancies(filter_vacancy))

    with open('./data/vacansies_hh.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    sj = SuperJobAPI()
    data_ = json.loads(sj.get_vacancies(filter_vacancy))

    with open('./data/vacansies_sj.json', 'w', encoding='utf-8') as file:
        json.dump(data_, file, ensure_ascii=False, indent=2)

    dict = {}
    list_hh = []
    list_sj = []
    for item_hh in data['items']:
        name = item_hh['name']
        url = item_hh['url']
        salary = item_hh['salary']
        requirements = item_hh['snippet']['requirement']
        vacancy = Vacancy(name, url, salary, requirements)

        list_hh.append(vacancy)

    for item_sj in data_['objects']:
        name = item_sj['profession']
        url = item_sj['link']
        salary = f'{item_sj["payment_from"]} - {item_sj["payment_to"]}'
        requirements = item_sj['candidat']
        vacancy = Vacancy(name, url, salary, requirements)

        list_sj.append(vacancy)



    # for item_hh in list_hh:
    #     print(item_hh)

    for item in list_sj:
        print(item)




user_interaction()


# if __name__ == "main.py":
#     user_interaction()
