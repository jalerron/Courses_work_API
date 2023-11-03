# from headhunter import HeadHunterAPI
#
# hh_api = HeadHunterAPI()
# hh_vacancies = hh_api.get_vacancies("Python")

# class MixinAPIOUT:
#
#     def get_response(self, response):
#
#         response =
#         return response.get_

class Vacancy:
    """
    Класс для вакансии

    """

    # vacancies = []

    def __init__(self, name: str, area: str, url: str, salary_to: int, salary_from: int, requirement: str) -> None:
        """
        Инициализация класса

        Args:
            name (_type_): str
            url (_type_): str
            salary (_type_): tuple
            requirement (_type_): str
        """
        self.name = name
        self.area = area
        self.url = url
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.requirement = requirement
        self.currency = None
        self.platform = None

        # for item in data['items']:
        #     vacancy = Vacancy(name=item['name'], url=item['url'], salary=item['salary'],
        #                       requirement=item['snippet']['requirement'])

        # Vacancy.vacancies.append(self)

    def __str__(self):
        return f'{self.name}'

    # def __repr__(self):
    #     return f'{self.name}'

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

# Добавить сравнения

#

#
# for item in hh_vacancies['items']:
#     name = item['name']
#     url = item['url']
#     salary = item['salary']
#     requirements = item['snippet']['requirement']
#
#     vacancy = Vacancy(name, url, salary, requirements)
