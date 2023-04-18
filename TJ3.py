from TJ2 import ConsultaProcessual

class TjAP_Tucujuris(ConsultaProcessual):
    
    def __init__(self, instancia='1'):
        self.UrlBase = 'http://tucujuris.tjap.jus.br/'
        self.UrlBusca = self.UrlBase + 'api/publico/buscar-autos-consulta-publica'       
        self.Tribunal = 'TjAP'
        self.Origem = 'tjap - tucujuris'
        self.Instancia = instancia
