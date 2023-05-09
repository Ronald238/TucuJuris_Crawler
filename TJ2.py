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
        
    
          data = dict()
          data['process_number'] = infos.get('cnj_number', '')
          data['process_class'] = infos.get('class', '')
          data['process_area'] = ''
          data['subject_process'] = subject
          data['process_value'] = infos.get('cause_value', '')
          data['vara_processo'] = infos.get('lotacao', '')
          data['parts'] = parts
          data['movements'] = moves
        
          return data
