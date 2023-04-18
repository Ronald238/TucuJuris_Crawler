from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def init(self, instancia='1'):
        pass

    @abstractmethod
    def request(self, method, url, params=None, data=None, headers=None):
        pass

    @abstractmethod
    def enter(self, username='', password='', instancia='', token=''):
        self.isLogin = True

    @abstractmethod
    def exit(self, type, value, traceback):
        pass

    @abstractmethod
    def start(self, **campos):
        pass

    @abstractmethod
    def buscar_links(self):
        pass

    ## Extrair dados da página e converter para json
    @abstractmethod
    def extrair_dados(self, link):
        pass

    @abstractmethod
    def salvar(self, valor):
        pass
