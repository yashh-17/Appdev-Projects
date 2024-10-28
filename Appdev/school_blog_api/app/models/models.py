# app/models.py

from pydantic import BaseModel
from datetime import datetime

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    author: str = "Admin"  # Default author
    created_at: datetime = datetime.now()
