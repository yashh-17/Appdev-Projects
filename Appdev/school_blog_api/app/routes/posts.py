# app/routes/posts.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import datetime

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    author: str = "Admin"  
    created_at: datetime = datetime.now()

router = APIRouter()

blog_posts = []

@router.post("/posts/", response_model=BlogPost)
def create_post(post: BlogPost):
    blog_posts.append(post)
    return post

@router.get("/posts/", response_model=List[BlogPost])
def get_posts():
    return blog_posts
