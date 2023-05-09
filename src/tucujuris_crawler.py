import time
import os
import requests
import json
import logging
from datetime import datetime
from TucuJuris_Crawler.src.base.Base import Base


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
          self.r = requests.session()
          return self
    
      def start(self, fields:dict):
          self.validate_fields(**fields)
          self.r = requests.session()
          response_link = self.search_links()
        
          number_failures = 0
          failures = list()
          total_data = list()
          for response in response_link:
              try:
                  data = self.extract_data(response)
                  total_data.append(data)
    
              except Exception as e:
                  number_failures += 1
                  failures.append(str(e))
                  print(e, number_failures)
          return total_data
        
        
      def validate_fields(self, **fields):
          self.Fields = fields
          self.Uf = fields.get('Uf', '').upper()
          self.Oab = fields.get('oab', '').upper()
          self.Name = fields.get('name', '').upper()
          self.Process = fields.get('process', '').upper()
          self.Oab_Uf = '{}{}'.format(self.Oab, self.Uf)
