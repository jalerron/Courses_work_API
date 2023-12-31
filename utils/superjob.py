# info:
#     ID	3137
#     Secret key	v3.r.137928314.de44b68cf145a1d94b50f46b0cc1e515e9d2030e.40956abe621d1de195432691420866bf2e5003ca
import os
import requests
from utils.abstract import abstract_api


class SuperJobAPI(abstract_api):
    """
    Класс для работы с API_Superjob.ru
    """
    __API_KEY: str = os.getenv('SJ_API_KEY')

    def __init__(self):
        """
        Инициализация класса
        """

        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.headers = {'X-Api-App-Id': self.__API_KEY}

    def get_vacancies(self, filter_vacancy: str):
        """
        Метод для получения вакансий
        """

        self.params = {"keyword": filter_vacancy}
        self.response = requests.get(self.url, self.params, headers=self.headers).json()["objects"]
        return self.response

    def filtered_vacancies(self):
        """
        Фильтрация вакансий по необходимым тегам
        """
        data = self.response
        filtered_vacancies = []

        for item in data:  # Создание словаря с одинаковым содержанием

            vacancy = {
                "platform": "SJ",
                "name": item["profession"],
                "area": item["town"]["title"],
                "url": item["link"],
                "salary_from": item["payment_from"],
                "salary_to": item["payment_to"],
                "currency": item["currency"],
                "requirement": item["candidat"].strip('\n')
            }

            filtered_vacancies.append(vacancy)

        return filtered_vacancies
