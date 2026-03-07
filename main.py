from fastapi import FastAPI, HTTPException,status,Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2  # Python library for conncetion with the database
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

while True:
    
    try:
        conn = psycopg2.connect(
            host= "localhost",
            database= "fastapi",
            user = 'postgres',
            password = 'root',
            cursor_factory= RealDictCursor )
         
        cursor = conn.cursor()
        print('Database connection was successful')
        break  
          
    except Exception as error:
        print('connection to database failed')
        err_str = str(error)
        print('error:', err_str)
        if 'password authentication failed' in err_str:
            print('wrong password')
        elif 'does not exist' in err_str or 'database' in err_str:
            print('database does not exist')
        elif 'role' in err_str or 'user' in err_str:
            print('user/role does not exist')
        else:
            print('unknown connection error')
        time.sleep(2)
        

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


 
posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

def find_post(id: int):
     for p in posts:
          if p["id"] == id:
               return p


def find_index_post(id: int):
    for i, p in enumerate(posts):
        if p["id"] == id:
            return i
       
@app.get("/posts")
def get_posts():
    # with conn.cursor() as cursor:
        cursor.execute(""" SELECT * FROM posts""")
        posts = cursor.fetchall()
        conn.commit()
        print(posts )
 
        return {"data": posts}
 
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    with conn.cursor() as cursor:  # create a new cursor for this request
        # to insert the new post to the posts table 
        cursor.execute( 
            "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
            (post.title, post.content, post.published)
        )
        new_post = cursor.fetchone()  # returns dict because of RealDictCursor
        conn.commit()  # save changes
    return {"data": new_post}
# @app.get('/posts/latest')
#  def get_post_latest():
#     if not posts:
#         raise HTTPException(status_code=404, detail="no posts")
#     latest_post = posts[-1]
#     return latest_post


@app.get('/posts/{id}')
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    tesr_post = cursor.fetchone()
    
    print(id)
    post = find_post(id)
    print(tesr_post)
    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    return {"post_detail": tesr_post}


# Update 
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(
        """UPDATE posts 
           SET title = %s, content = %s, published = %s 
           WHERE id = %s 
           RETURNING *""",
        (post.title, post.content, post.published, id)
    )

    updated_post = cursor.fetchone()

    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    conn.commit()

    return {"data": updated_post}

# Delete
@app.delete('/posts/{id}')
def delete_post(id : int):
    cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id)) )
    deleted_post = cursor.fetchone()
    conn.commit()
    index = find_index_post(id)
    
    if index is None:
        raise HTTPException(status_code=404, detail= "Post not found")
    
    deleted_post = posts.pop(index)
    return {"message": "Post deleted successfully",
             "data": deleted_post}
    
     
     


