# from utils.abstract import Req_api
import requests
import json
# import pandas as pd

class HeadHunterAPI():
    """
    Клас для работы с API_HH
    """
    def __init__(self) -> None:
        pass

    def get_vacancies(self, filter_vacancy: str):
        """
        Метод для получения вакансий
        """
        self.params = {"text": filter_vacancy}
        self.response = requests.get('https://api.hh.ru/vacancies', self.params).content.decode()
        data = json.loads(str(self.response))
        return data

    
# hh = HeadHunterAPI()
#
# print(type(hh.get_vacancies("Python")))
#
# data = json.loads(hh.get_vacancies("Python"))
#
# # df = pd.DataFrame(data)
#
# with open('vacansies.json', 'w', encoding='utf-8') as fp:
#     json.dump(data, fp, ensure_ascii=False, indent=4)
#

# print(df)