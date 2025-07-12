from fastapi import Response,status,HTTPException, Depends, APIRouter
from . . import models,schemas
from sqlalchemy.orm import Session
from . . database import get_db
from typing import List,Optional
from . auth2 import get_current_user
from sqlalchemy import func
router = APIRouter(
    prefix='/posts',
    tags=['posts']
)
@router.get("/",response_model=List[schemas.PostVote])

def test_posts(db:Session = Depends(get_db), current_user:int = Depends(get_current_user),limit:int =10,skip:int=0, search:Optional[str]=""):

    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # # #print(limit)

    results = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()


    
    return results



# @router.get("/posts")
# def get_posts():
    # cursor.execute(""" select * from posts """)
    # posts = cursor.fetchall()
    
    # return {"Data":posts}


@router.post("/",response_model=schemas.Post)
def create_post(post:schemas.PostCreat,db:Session = Depends(get_db), current_user:int = Depends(get_current_user)):
    
#     cursor.execute(""" insert into posts (title, content, published)
#                    values(%s,%s,%s) returning * """,(new_post.title, new_post.content, new_post.Published))
    
#     new_post = cursor.fetchone()
#     conn.commit()

#     return{"data":new_post}  
    
    print(current_user.email, current_user.id)
    np = models.Post(owner_id=current_user.id,**post.dict())
    db.add(np)
    db.commit()
    db.refresh(np)
    return np


@router.get("/{id}",response_model=schemas.PostVote) 
def get_post(id:int, db:Session = Depends(get_db)):
    

    # cursor.execute(""" select * from posts where id = %s """,(str(id)))
    # post = cursor.fetchone()
    # print(post)

    post = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()


    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"messege":"maal pai ni"})
        
    return post


@router.delete("/{id}")
def delete_post(id:int,db:Session = Depends(get_db), current_user:int = Depends(get_current_user)):

    # cursor.execute(""" delete from posts where id = %s returning * """,(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    delete_post=db.query(models.Post).filter(models.Post.id == id)
    post = delete_post.first()


    if delete_post.first() ==  None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="lokre bol sign in korte")
    
    delete_post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,post:schemas.PostCreat,db:Session = Depends(get_db), current_user:int = Depends(get_current_user)):

    # cursor.execute(""" update posts set title = %s, content = %s where id = %s returning *""", (post.title,post.content,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    updated_post = db.query(models.Post).filter(models.Post.id == id)
    pp = updated_post.first()
    if pp == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")

    if pp.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="lokre bol sign in korte")
    
    updated_post.update(post.dict(),synchronize_session=False)
    
    db.commit()
    
    # post_dict = post.dict()
    # print(post_dict)
    # post_dict['id'] = id
    
    return updated_post.first() 
