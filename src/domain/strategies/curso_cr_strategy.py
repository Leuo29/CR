from abc import ABC, abstractmethod

class CursoCRStrategy(ABC):
    @abstractmethod
    def calcular_media(self, curso):
        pass
