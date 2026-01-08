from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import blog_schema
from app.models import blog as blog_model
from app.config.database import get_db

# Router banao - saare blog related endpoints yahan rahenge
router = APIRouter(prefix="/blog", tags=["Blog"])


@router.post("/")
def create_blog(request: blog_schema.Blog, db: Session = Depends(get_db)):
    """Naya blog create karo"""
    new_blog = blog_model.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/blog")
def get_all_blogs(db: Session = Depends(get_db)):
    """Saare blogs fetch karo"""
    blogs = db.query(blog_model.Blog).all()
    return blogs
@router.get("/blog/{id}")
def show(id:int,db:Session=Depends(get_db)):
    blog=db.query(blog_model.Blog).filter(blog_model.Blog.id==id).first() # = = y tha = nahi 
    return blog