# info:
#     ID	3137
#     Secret key	v3.r.137928314.de44b68cf145a1d94b50f46b0cc1e515e9d2030e.40956abe621d1de195432691420866bf2e5003ca
import requests
import json
from utils.abstract import abstract_api


class SuperJobAPI(abstract_api):
    """
    Класс для работы с API_Superjob.ru
    """
    API_KEY = "v3.r.137928314.de44b68cf145a1d94b50f46b0cc1e515e9d2030e.40956abe621d1de195432691420866bf2e5003ca"

    def __init__(self):
        """
        Инициализация класса
        """

        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.headers = {'X-Api-App-Id': self.API_KEY}

    def get_vacancies(self, filter_vacancy: str):
        """
        Метод для получения вакансий
        """

        self.params = {"keyword": filter_vacancy}
        self.response = requests.get(self.url, self.params, headers=self.headers).content.decode()
        return self.response


