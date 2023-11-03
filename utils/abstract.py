from abc import ABC, abstractmethod


class abstract_api(ABC):

    @abstractmethod
    def get_vacancies(self, filter_vacancy):
        pass

    @abstractmethod
    def filtered_vacancies(self):
        pass
