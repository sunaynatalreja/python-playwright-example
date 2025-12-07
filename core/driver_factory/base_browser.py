from abc import ABC, abstractmethod

class BrowserBase(ABC):
    @abstractmethod
    def get_browser(self):
        """ Provide the code for launching browser """
        pass