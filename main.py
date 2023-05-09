from fastapi import FastAPI, Request
from TJ3 import TjAP_Tucujuris

client = TjAP_Tucujuris()
app = FastAPI()

# with TjAP_Tucujuris() as t:
# t.start(name='Joao Rosa')
 
@app.get("/hello")
def root():
          return {"messege": "Hello World"}

@app.post("/query")
async def query(request: Request):
      # try:
          form = await request.json()
        
          print(form)
          data = client.start(form)
        
          return {'processes': data}
      # except Exception as e:
      # return error(msg=e.args[0])

def get_content(content, required_fields):
      validate_content(content, required_fields)
      return content

def validate_content(content, required_fields):
      for field in required_fields:
          if field not in content:
              print(field)
              raise print("Invalid request.")

def error(msg="Unknown error processing request."):
      return {
          "success" : False,
          "msg": msg
      }
            
def invalid_request():
      return error(msg="Invalid request.")

def ok():
      return {
          "success" : True
      }
