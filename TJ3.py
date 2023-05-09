from TJ2 import ProceduralConsultation

class TjAP_Tucujuris(ProceduralConsultation):
    
     def __init__(self, instance='1'):
         self.UrlBase = 'http://tucujuris.tjap.jus.br/'
         self.UrlBusca = self.UrlBase + 'api/publico/buscar-autos-consulta-publica'
         self.Court = 'TjAP'
         self.Origem = 'tjap - tucujuris'
         self.Instance = instance
