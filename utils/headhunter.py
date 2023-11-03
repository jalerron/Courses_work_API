import requests
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
        self.response = requests.get(self.url, self.params).json()["items"]
        return self.response

    def filtered_vacancies(self):
        """
        Фильтрация вакансий по необходимым тегам
        """
        data = self.response
        filtered_vacancies = []

        for item in data:
            if item["salary"]:
                salary_from = item["salary"]["from"] if item["salary"]["from"] else 0
                salary_to = item["salary"]["to"] if item["salary"]["to"] else 0
                currency = item["salary"]["currency"] if item["salary"]["currency"] else "null"
            else:
                salary_to = 0
                salary_from = 0
                currency = "null"

            vacancy = {
                "platform": "HH",
                "name": item["name"],
                "area": item["area"]["name"],
                "url": item["url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "currency": currency,
                "requirement": item["snippet"]["requirement"]
            }

            filtered_vacancies.append(vacancy)

        return filtered_vacancies


# Отфильтровать зарплату (убрать null)


# hh = HeadHunterAPI()
# hh.get_vacancies("python")
# print(hh.filtered_vacancies())
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
