from fastAPI import FastAPI

app = FastAPI()

@app.get("/")
def read_root() :
  return {"message": "a dance of fire and ice"}