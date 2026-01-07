from fastapi import FastAPI
import uvicorn
import schema as schemas
import model as models
from database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def me():
    return {"message": "This is my world"}


@app.post("/blog")
def myblog(request: schemas.Blog):
    return request


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
