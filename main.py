from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_info():
    return {"hell":"o"}

@app.get("/nn")
def get_info():
    return {"hellm":"omm"}