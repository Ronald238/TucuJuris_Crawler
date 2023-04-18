import time
import os
import requests
import json
import logging
from datetime import datetime
from Base import Base


logging.basicConfig(level=logging.INFO)

class Tucujuris():
    
    def request(self, method, url, params=None, data=None, headers=None, timeout=30):
        
        if method == 'post':
            response = self.r.post(url, data=data, headers=headers, timeout=timeout)
        elif method == 'get':
            response = self.r.get(url, params=params, headers=headers, timeout=timeout)
        else:
            raise Exception('Método inválido')
                
        return response
    
    def __exit__(self, type, value, traceback):
        self.r.close()
    
    def __enter__(self):
        print("batata")
        self.r = requests.session()
        return self
    
    def start(self, campos:dict):
        self.normalizar_campos(**campos)
        self.r = requests.session()
        response_link = self.buscar_links() 
        
        qnt_falhas = 0
        falhas = list()
        total_dados = list()
        for response in response_link:
            try:
                dados = self.extrair_dados(response)
                total_dados.append(dados)
    
            except Exception as e:
                qnt_falhas += 1
                falhas.append(str(e))
                print(e, qnt_falhas)
        return total_dados
        
    def normalizar_campos(self, **campos):
        Uf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',  'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        
        self.Campos = campos

        
        self.Uf = campos.get('Uf', '').upper()
        self.UfIndex = Uf.index(self.Uf) if self.Uf in Uf else None        
        self.Oab = campos.get('oab', '').upper()
        self.Nome = campos.get('nome', '').upper()
        self.Documento = campos.get('documento', '').upper()
        self.Processo = campos.get('processo', '').upper()
        self.Oab_Uf = '{}{}'.format(self.Oab, self.Uf)
        self.Uf_OAB = '{}-{}'.format(self.Uf, self.Oab)
        self.UfOAB = '{}{}'.format(self.Uf, self.Oab.zfill(6))