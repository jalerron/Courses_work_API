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

class Vacancy():
    """
    Класс для вакансии

    """

    # vacancies = []

    def __init__(self, name: str, url: str, salary: str, requirement: str) -> None:
        """
        Инициализация класса

        Args:
            name (_type_): str
            url (_type_): str
            salary (_type_): tuple
            requirement (_type_): str
        """
        self.name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement

        # for item in data['items']:
        #     vacancy = Vacancy(name=item['name'], url=item['url'], salary=item['salary'],
        #                       requirement=item['snippet']['requirement'])

        # Vacancy.vacancies.append(self)

    def __str__(self):
        return f'{self.name}, {self.salary}, {self.url}'

    def __repr__(self):
        return f'{self.name}'

#

#
# for item in hh_vacancies['items']:
#     name = item['name']
#     url = item['url']
#     salary = item['salary']
#     requirements = item['snippet']['requirement']
#
#     vacancy = Vacancy(name, url, salary, requirements)