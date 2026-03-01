from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

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
    

@app.post("/posts")    
def create_posts(post: Post):
    new_post = post.dict()
    new_post["id"] = len(posts) + 1
    posts.append(new_post)

    print(f"""
    Id: {new_post['id']}
    Title: {new_post['title']}
    Content: {new_post['content']}
    Is Published: {new_post['published']}
    """)

    return new_post


# @app.get('/post/{id}')
# def get_posts_id(post_id : Post):
     
