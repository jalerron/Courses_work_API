from utils.vacancy import Vacancy
import json

class JSONSaver:
    """
    Класс для Json
    """

    def __init__(self):
        self.type: bool

    def save_to_json(self, response):
        """
        Запись вакансий в Json
        """
        #
        # with open('../datavacansies.json', 'w', encoding='utf-8') as file:
        #     json.dump(response, file, ensure_ascii=False, indent=2)


# vacancy = Vacancy('Python', 'url', '100000руб', 'blabla')
# print(vacancy)
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
