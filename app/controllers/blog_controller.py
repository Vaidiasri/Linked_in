from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas import blog_schema
from app.models import blog as blog_model
from app.config.database import get_db

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.post(
    "/", response_model=blog_schema.BlogOut, status_code=status.HTTP_201_CREATED
)
def create_blog(request: blog_schema.Blog, db: Session = Depends(get_db)):
    """Naya blog create karo"""
    new_blog = blog_model.Blog(
        title=request.title, body=request.body, user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/", response_model=List[blog_schema.BlogOut])
def get_all_blogs(db: Session = Depends(get_db)):
    """Saare blogs get karo"""
    return db.query(blog_model.Blog).all()


@router.get("/{id}", response_model=blog_schema.BlogOut)
def get_blog(id: int, db: Session = Depends(get_db)):
    """Ek specific blog get karo"""
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    return blog


@router.put("/{id}", response_model=blog_schema.BlogOut)
def update_blog(id: int, request: blog_schema.Blog, db: Session = Depends(get_db)):
    """Blog update karo"""
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )

    blog.title = request.title
    blog.body = request.body
    if request.user_id is not None:
        blog.user_id = request.user_id

    db.commit()
    db.refresh(blog)
    return blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    """Blog delete karo"""
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )

    db.delete(blog)
    db.commit()
    return None
