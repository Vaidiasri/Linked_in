from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

from app.schemas import blog_schema
from app.models import blog as blog_model
from app.config.database import get_db

router = APIRouter(prefix="/blog", tags=["Blog"])


# POST api
@router.post("/", response_model=blog_schema.BlogOut)
def create_blog(request: blog_schema.Blog, db: Session = Depends(get_db)):
    new_blog = blog_model.Blog(
        title=request.title,
        body=request.body,
        user_id=request.user_id,  # Set user_id if provided
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# GET all blogs
@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[blog_schema.BlogOut]
)
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(blog_model.Blog).options(joinedload(blog_model.Blog.owner)).all()
    return blogs


# GET blog by id
@router.get("/{id}", response_model=blog_schema.BlogOut)
def show(id: int, db: Session = Depends(get_db)):
    blog = (
        db.query(blog_model.Blog)
        .options(joinedload(blog_model.Blog.owner))
        .filter(blog_model.Blog.id == id)
        .first()
    )
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} does not exist",
        )
    return blog


# DELETE blog by id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id).first()
    if not blog:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    db.delete(blog)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: blog_schema.Blog, db: Session = Depends(get_db)):
    blog = db.query(blog_model.Blog).filter(blog_model.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )

    blog.update({"title": request.title, "body": request.body})

    db.commit()
    return {"detail": "Blog updated successfully"}
