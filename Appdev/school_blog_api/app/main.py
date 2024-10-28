from fastapi import FastAPI, HTTPException
from starlette.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="../static"), name="static")

MONGODB_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGODB_URL)
db = client.school_blog

class BlogPost(BaseModel):
    title: str
    content: str

class BlogPostInDB(BlogPost):
    id: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("../static/index.html") as f:
        return f.read()

@app.post("/posts/", response_model=BlogPostInDB)
async def create_post(post: BlogPost):
    post_dict = post.dict()
    result = await db.posts.insert_one(post_dict)
    created_post = BlogPostInDB(id=str(result.inserted_id), **post_dict)
    return created_post

@app.get("/posts/", response_model=List[BlogPostInDB])
async def get_posts():
    posts = []
    async for post in db.posts.find():
        post["id"] = str(post["_id"])
        posts.append(BlogPostInDB(**post))
    return posts
