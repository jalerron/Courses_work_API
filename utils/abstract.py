from abc import ABC, abstractmethod


class abstract_api(ABC):

    @abstractmethod
    def get_vacancies(self, filter_vacancy):
        pass

    # @abstractmethod
    # def save_to_json(self, data, file):
    #     pass

# class Req_api(ABC):
#
#     @abstractmethod
#     def get_req(self):
#         pass