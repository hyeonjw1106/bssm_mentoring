from fastAPI import FastAPI

app = FastAPI()

@app.get("/")
def read_root() :
  return {"message": "I'm eminem. godzilla!"}