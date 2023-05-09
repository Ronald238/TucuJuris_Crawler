import time
import os
import requests
import json
import logging
from datetime import datetime
from Base import Base


logging.basicConfig(level=logging.INFO)

class Tucujuris():
    
      def require(self, method, url, params=None, data=None, headers=None, timeout=30):
        
          if method == 'post':
              response = self.r.post(url, data=data, headers=headers, timeout=timeout)
          elif method == 'get':
              response = self.r.get(url, params=params, headers=headers, timeout=timeout)
          else:
              raise Exception('Invalid method')
                
          return response
    
      def __exit__(self, type, value, traceback):
          self.r.close()
    
      def __enter__(self):
          print("potato")
          self.r = requests.session()
          return self
    
      def start(self, fields:dict):
          self.validate_fields(**fields)
          self.r = requests.session()
          response_link = self.search_links()
        
          qnt_failures = 0
          failures = list()
          total_data = list()
          for response in response_link:
              try:
                  data = self.extract_data(response)
                  total_data.append(data)
    
              except Exception as e:
                  number_failures += 1
                  failures.append(str(e))
                  print(e, how many_failures)
          return total_data
        
      def validate_fields(self, **fields):
          Uf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS' , 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', ' SP', 'SE', 'TO']
        
          self.Fields = fields

        
          self.Uf = fields.get('Uf', '').upper()
          self.UfIndex = Uf.index(self.Uf) if self.Uf in Uf else None
          self.Oab = fields.get('oab', '').upper()
          self.Name = fields.get('name', '').upper()
          self.Document = fields.get('document', '').upper()
          self.Process = fields.get('process', '').upper()
          self.Oab_Uf = '{}{}'.format(self.Oab, self.Uf)
          self.Uf_OAB = '{}-{}'.format(self.Uf, self.Oab)
          self.UfOAB = '{}{}'.format(self.Uf, self.Oab.zfill(6))
