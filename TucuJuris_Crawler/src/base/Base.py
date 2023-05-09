from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def init(self, instancia='1'):
        pass

    @abstractmethod
    def require(self, method, url, params=None, data=None, headers=None):
        pass

    @abstractmethod
    def enter(self):
        pass
    @abstractmethod
    def exit(self, type, value, traceback):
        pass

    @abstractmethod
    def start(self, **fields):
        pass

    @abstractmethod
    def fetch_links(self):
        pass

    @abstractmethod
    def extract_data(self, link):
        pass
