from fastapi import FastAPI
import uvicorn

from app.config.database import engine, Base
from app.controllers import blog_router, user_router, login_router

# FastAPI app initialize karo
app = FastAPI(
    title="Blog API",
    description="FastAPI blog application with MVC structure",
    version="1.0.0",
)

# Database tables create karo
Base.metadata.create_all(bind=engine)


# Root endpoint
@app.get("/")
def root():
    """Welcome endpoint"""
    return {"message": "This is my world"}


# Controllers ko include karo
app.include_router(blog_router)
app.include_router(user_router)
app.include_router(login_router)            


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
