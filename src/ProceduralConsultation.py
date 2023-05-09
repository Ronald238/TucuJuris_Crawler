from src.tucujuris_crawler import Tucujuris
from datetime import datetime

class ProceduralConsultation(Tucujuris):
    def __init__(self):
          self.Court = 'AP'
          self.UrlBase = 'http://tucujuris.tjap.jus.br/'
          self.UrlBusca = self.UrlBase + 'api/publico/consultar-processos'
          self.Header = {}


    def fetch_links(self):
        captcha = self.require('get', "http://tucujuris.tjap.jus.br/api/publico/buscar-passe-captcha").json()
        payload = {'nome_parte': '', 'documento_parte': '',
                    'numero_carta_precatoria': '', 'situacao_processo': '', 'captcha': captcha['data']}

        if self.Oab and self.Uf:
            payload['oab_advogado'] = self.Oab_Uf

        elif self.Name:
            payload['nome_advogado'] = self.Name
    
        elif self.Process != '':
            payload['numero_unico'] = self.Process

        self.Header = {"Content-Type": "application/json"}
        response = self.require('get', self.UrlBusca, params=payload, headers=self.Header).json()
        links = []
        for i in response['data'].get('autos'):
            links.append({'autos_id': i.get('id'),
                        'chave_consumo': ''})
        return links
      

    def get_process_number(self, infos: dict) -> str:
        return infos.get('cnj_number', '')


    def get_process_class(self, infos: dict) -> str:
        return infos.get('class', '')


    def get_process_value(self, infos: dict) -> str:
        return infos.get('cause_value', '')


    def get_vara_processo(self, infos: dict) -> str:
        return infos.get('lotacao', '')
    

    def get_subject_process(self, infos: dict):
        try:
            subject = infos['cnj_subject'][0].get('description', '')
        except:
            subject = ''
        return subject
    
    
    def get_parts(self, infos):
        return infos['dados']['capa']

    
    def process_movements(data):
        movements = []
        for i in data['data']['movements']:
            progress = i.get('complemento_pa')
            time = time.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ') if time is not None else ''
            date = i.get('dt_andamento_pa').split(' ')[0]
            movements.append({
                'title': i.get('description_pa').replace('\n', ' ').replace('\r', ' ').replace('\t', ' '),
                'content': progress,
                'date': datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y'),
                'complement': ''
            })
        return movements


    def extract_data(self, response):
        data = self.require('GET', self.UrlBase + 'api/publico/buscar-details-autos-consulta-publica',
                             params=response, headers=self.Header).json()
    
        if 'mensagem' in data and data['mensagem'].startswith(''):
            return {}
        infos = data['dados']['cabecalho']
        parts = data['dados']['capa']

        return {
            "process_number":  self.get_process_number(infos),
            "process_class": self.get_process_class(infos),
            "process_area": None,
            "subject_process": self.get_subject_process(data),
            "process_value": self.get_process_value(infos),
            "vara_processo":self. get_vara_processo(infos),
            "parts": self.get_parts(parts),
            "movements": self.process_movements(data)
        }
    
          
