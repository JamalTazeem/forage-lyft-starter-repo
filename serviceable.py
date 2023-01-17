from abc import ABC, abstractmethod

class serviceable(ABC):
    def needs_service(self):
        pass