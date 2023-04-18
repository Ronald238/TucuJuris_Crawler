from fastapi import FastAPI, Request
from TJ3 import TjAP_Tucujuris

client = TjAP_Tucujuris()
app = FastAPI()

# with TjAP_Tucujuris() as t:
#     t.start(nome='Joao Rosa')
 
@app.get("/hello")
def root():
        return {"messege": "Hello World"}

@app.post("/consulta")
async def consulta(request: Request):
    # try:
        form = await request.json()
        
        print(form)
        dados = client.start(form)
        
        return {'processos': dados}
    # except Exception as e:
    #     return error(msg=e.args[0]) 

def get_content(content, required_fields):
    validate_content(content, required_fields)
    return content

def validate_content(content, required_fields):
    for field in required_fields:
        if field not in content:
            print(field)
            raise print("Requisição inválida.")

def error(msg="Erro desconhecido ao processar requisição."):
    return {
        "sucesso" : False,
        "msg": msg
    }
            
def invalid_request():
    return error(msg="Requisição inválida.")

def ok():
    return {
        "sucesso" : True
    }
