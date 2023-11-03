from utils.vacancy import Vacancy
import json
from pathlib import Path

ROOT = Path('../').parent
DATA_PATH = Path.joinpath(ROOT, 'data')
FILE_PATH = Path.joinpath(DATA_PATH, 'vacansies.json')
path = FILE_PATH

class JSONSaver:
    """
    Класс для работы с Json
    """

    def save_to_json(self, data):
        """
        Запись вакансий в Json-файл
        """

        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def read_from_file(self, filename: str):
        """
        Чтение данных из файла с созданием экземпляров класса
        """
        with open(filename, 'r', encoding='utf-8') as fp:
            data = json.load(fp)

        vacancies_list = []

        for item in data:  # Создание экземпялов класса Vacancy
            vacancy = Vacancy(
                name=item["name"],
                area=item["area"],
                url=item["url"],
                salary_from=item["salary_from"],
                salary_to=item["salary_to"],
                requirement=item["requirement"],
                currency=item["currency"]
            )
            vacancy.platform = item["platform"]

            vacancies_list.append(vacancy)

        return vacancies_list
