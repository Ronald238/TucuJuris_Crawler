from TJ1 import Tucujuris
from datetime import datetime
import time

class ConsultaProcessual(Tucujuris):
    
    def __init__(self):
        self.Tribunal = 'AP'
        self.UrlBase = 'http://tucujuris.tjap.jus.br/'
        self.UrlBusca = self.UrlBase + 'api/publico/consultar-processos'
        self.Header = {}

    def buscar_links(self):
        print("BUSCAR LINKS")

        captcha = self.request('get', "http://tucujuris.tjap.jus.br/api/publico/buscar-passe-captcha").json()
        payload = {'nome_parte': '', 'documento_parte': '',
                   'numero_carta_precatoria': '', 'situacao_processo': '', 'captcha': captcha['dados']}

        if self.Oab and self.Uf:
            payload['oab_advogado'] = self.Oab_Uf

        elif self.Nome:
            payload['nome_advogado'] = self.Nome

        elif self.Documento:
            return []
        
        elif self.Processo != '':
            payload['numero_unico'] = self.Processo

        self.Header = {"Content-Type": "application/json"}
        response = self.request('get', self.UrlBusca, params=payload, headers=self.Header).json()
        links = []
        for i in response['dados'].get('autos'):
            links.append({'autos_id': i.get('id'),
                          'chave_consumo': ''})
        return links

    def extrair_dados(self, response):
        time.sleep(1)
        data = self.request('get', self.UrlBase + 'api/publico/buscar-detalhes-autos-consulta-publica', params=response, headers=self.Header).json()
        
        
        
        if 'mensagem' in data and data['mensagem'].startswith(''):
            return {}
        infos = data['dados']['cabecalho']
        partes = data['dados']['capa']

        dados = dict()
        movimentacao = list()    
        for i in data['dados']['movimentos']:
            andamento = i.get('complemento_pa')
            andamento = andamento.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ') if andamento != None else ''
            data = i.get('dt_andamento_pa').split(' ')[0]
            movimentacao.append({'titulo': i.get('descricao_pa').replace('\n', ' ').replace('\r', ' ').replace('\t', ' '),
                   'conteudo': andamento,
                   'data': datetime.strptime(data,'%Y-%m-%d').strftime('%d/%m/%Y'),
                   'complemento': ''})
        
        if 'valor_causa' in infos:
            infos['valor_causa'] = int(infos['valor_causa'])
        try: assunto =  infos['cnj_assunto'][0].get('descricao', '')
        except: assunto = ''
        
    
        dados = dict()
        dados['numero_processo'] = infos.get('numero_cnj', '')
        dados['classe_processo'] = infos.get('classe', '')
        dados['area_processo'] = ''
        dados['assunto_processo'] = assunto
        dados['valor_processo'] = infos.get('valor_causa', '')
        dados['vara_processo'] = infos.get('lotacao', '')
        dados['partes'] = partes
        dados['movimentacoes'] = movimentacao
        
        return dados
