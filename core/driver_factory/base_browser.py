from abc import ABC, abstractmethod

class BrowserBase(ABC):
    @abstractmethod
    def get_page(self):
        """ Provide the code for launching browser """
        pass

    @abstractmethod
    def stop(self):
        """Provide the code for stop playwright instance and browser """
        pass