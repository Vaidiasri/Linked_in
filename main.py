from fastapi import FastAPI
import uvicorn
import schema as schemas

app = FastAPI()


@app.get("/")
def me():
    return {"message": "This is my world"}


@app.post("/blog")
def myblog(request: schemas.Blog):
    return request


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
