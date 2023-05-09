from TJ1 import Tucujuris
from datetime import datetime
import time

class ProceduralConsultation(Tucujuris):
    
      def __init__(self):
          self.Court = 'AP'
          self.UrlBase = 'http://tucujuris.tjap.jus.br/'
          self.UrlBusca = self.UrlBase + 'api/publico/consultar-processos'
          self.Header = {}

      def fetch_links(self):
          print("SEARCH LINKS")

          captcha = self.request('get', "http://tucujuris.tjap.jus.br/api/publico/buscar-passe-captcha").json()
          payload = {'part_name': '', 'part_document': '',
                     'number_letter_precatory': '', 'situacao_processo': '', 'captcha': captcha['data']}

          if self.Oab and self.Uf:
              payload['oab_advogado'] = self.Oab_Uf

          elif self.Name:
              payload['lawyer_name'] = self.Name

          elif self.Document:
              return[]
        
          elif self.Process != '':
              payload['unique_number'] = self.Process

          self.Header = {"Content-Type": "application/json"}
          response = self.request('get', self.UrlBusca, params=payload, headers=self.Header).json()
          links = []
          for i in response['data'].get('autos'):
              links.append({'autos_id': i.get('id'),
                            'consumption_key': ''})
          return links

      def extract_data(self, response):
          time.sleep(1)
          data = self.request('get', self.UrlBase + 'api/publico/buscar-details-autos-consulta-publica', params=response, headers=self.Header).json()
        
        
        
          if 'message' in data and data['message'].startswith(''):
              return {}
          infos = data['data']['header']
          parts = data['data']['cover']

          date = dict()
          move = list()
          for i in data['data']['movements']:
              progress = i.get('complemento_pa')
              time = time.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ') if time != None else ''
              data = i.get('dt_andamento_pa').split(' ')[0]
              movement.append({'title': i.get('description_pa').replace('\n', ' ').replace('\r', ' ').replace('\t', ' ') ,
                     'content': progression,
                     'date': datetime.strptime(date,'%Y-%m-%d').strftime('%d/%m/%Y'),
                     'complement': ''})
        
          if 'cause_value' in infos:
              infos['cause_value'] = int(infos['cause_value'])
          try: subject = infos['cnj_subject'][0].get('description', '')
          except: subject = ''
        
        
    def get_process_number(infos: dict) -> str:
        return infos.get('cnj_number', '')

    def get_process_class(infos: dict) -> str:
        return infos.get('class', '')

    def get_process_area() -> str:
        return ''

    def get_subject_process(subject: str) -> str:
        return subject

    def get_process_value(infos: dict) -> str:
        return infos.get('cause_value', '')

    def get_vara_processo(infos: dict) -> str:
        return infos.get('lotacao', '')

    def get_parts(parts: list) -> list:
        return parts

    def get_movements(moves: list) -> list:
        return moves

    data = {}
    data['process_number'] = get_process_number(infos)
    data['process_class'] = get_process_class(infos)
    data['process_area'] = get_process_area()
    data['subject_process'] = get_subject_process(subject)
    data['process_value'] = get_process_value(infos)
    data['vara_processo'] = get_vara_processo(infos)
    data['parts'] = get_parts(parts)
    data['movements'] = get_movements(moves)


    return data
