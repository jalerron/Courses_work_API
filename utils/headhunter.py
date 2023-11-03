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

        for item in data:  # Создание словаря с одинаковым содержанием

            # Избавляемся от проблем с зарплатой типа null
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
                "url": item["alternate_url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "currency": currency,
                "requirement": item["snippet"]["requirement"]
            }

            filtered_vacancies.append(vacancy)

        return filtered_vacancies
