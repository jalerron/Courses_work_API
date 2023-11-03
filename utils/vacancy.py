class Vacancy:
    """
    Класс для вакансий
    """

    def __init__(self, name: str, area: str, url: str,  salary_from: int, salary_to: int, currency,
                 requirement: str) -> None:
        """
        Инициализация класса Vacancy
        """
        self.__name = name
        self.__area = area
        self.__url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement
        self.currency = currency
        self.platform = None

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def area(self):
        return self.__area

    def __str__(self):
        return f'{self.name}'

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from
