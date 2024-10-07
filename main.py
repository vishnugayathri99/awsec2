import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def Hello():
    return ("Hello world")

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=2)
