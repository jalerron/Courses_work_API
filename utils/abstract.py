from abc import ABC, abstractmethod



class Req_api(ABC):
    
    @abstractmethod
    def get_req(self):
        pass