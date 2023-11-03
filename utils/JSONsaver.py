from utils.vacancy import Vacancy
import json


class JSONSaver:
    """
    Класс для Json
    """

    def save_to_json(self, data):
        """
        Запись вакансий в Json
        """
        path = './data/vacansies.json'
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def read_from_file(self, filename: str):
        """
        Чтение данных из файла с созданием экземпляров класса
        """
        with open(filename, 'r', encoding='utf-8') as fp:
            data = json.load(fp)

        vacancies_list = []

        for item in data:
            vacancy = Vacancy(
                name=item["name"],
                area=item["area"],
                url=item["url"],
                salary_from=item["salary_from"],
                salary_to=item["salary_to"],
                requirement=item["requirement"]
            )
            vacancy.currency = item["currency"]
            vacancy.platform = item["platform"]

            vacancies_list.append(vacancy)

        return vacancies_list
# лоавбить метод чтения из файла, который сразу содзаст лист экземпляров вакансий(либо поделить)


# vacancy = Vacancy('Python', 'url', '100000руб', 'blabla')
# print(vacancy)
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
