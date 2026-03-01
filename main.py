from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"Hello": "wellcome to my api, hehe I am nathy cuze i am love codding an i am learning fastapi frameworks"}
  

# @app.get("/posts")
# def get_post():
#     return {"data": "this is a post method:"}

# class Post(BaseModel):
#      title:str
#      content: str
# @app.post("/createpost")
# def create_post(playload :Post):
#     print(playload.content)
#     return {"message": f"Post created with title '{playload.title}' and content '{playload.content}'"}
 
# name = "nathy"
# @app.get("/greet/{name}")
# def greeting(name: str):
#      return {"message" : f"Hello papa, wellcome to my api"}
    
 
posts = []

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
#     rating: Optional[int] = None

my_posts = [ {"title ": "title of post 1", "content": "content of post 1", "id": 1}, {"title ": "favorite foods", "content": "I like pizza", "id": 2} ]

def find_post(id):
     for p in my_posts:
          if p["id"] == id:
               return p


     

@app.post("/posts")    
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 10000000)
    posts.append(post_dict)
    return {"data": post_dict}


@app.get('/posts/{id}')
def get_post(id: int):
     print(id)
     post = find_post(id)
     print(post)
     return {"post_detail": post}
     


