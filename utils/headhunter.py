import requests
import json
from utils.abstract import abstract_api


class HeadHunterAPI(abstract_api):
    """
    Клас для работы с API_HH
    """

    def __init__(self) -> None:
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, filter_vacancy: str):
        """
        Метод для получения вакансий
        """
        self.params = {"text": f"NAME:{filter_vacancy}"}
        self.response = requests.get(self.url, self.params).content.decode()
        return self.response

# Отфильтровать зарплату (убрать null)


# hh = HeadHunterAPI()
#
# print(type(hh.get_vacancies("Python")))
#
# data = json.loads(hh.get_vacancies("Python"))
#
# list_vacancy = []
# for item in data['items']:
#     vacancy = Vacancy(name=item['name'], url=item['url'], salary=item['salary'],
#                       requirement=item['snippet']['requirement'])
#     dict_ = {
#         "name": vacancy.name,
#         "url": vacancy.url,
#         "salary": vacancy.salary,
#         "requirement": vacancy.requirement
#     }
#     list_vacancy.append(dict_)
#
# for item in list_vacancy:
#     print(item)

# with open('vacansies2.json', 'w+', encoding='utf-8') as file:
#     json.dump(list_vacancy, file, ensure_ascii=False, indent=4)
# # df = pd.DataFrame(data)
#
#

# print(df)
