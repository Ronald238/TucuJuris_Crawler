from fastapi import FastAPI, Request
from src.init import TjAP_Tucujuris

client = TjAP_Tucujuris()
app = FastAPI()

@app.get("/hello")
def root():
          return {"messege": "Hello World"}

@app.post("/query")
async def query(request: Request):
      try:
          form = await request.json()
          data = client.start(form)
          return {'processes': data}
      except Exception as e:
            return error(msg=e.args[0])

#   Utils
##################################################################

def error(msg="Unknown error processing request."):
      return {
          "success" : False,
          "msg": msg
      }
