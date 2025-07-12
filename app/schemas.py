
from pydantic import BaseModel, EmailStr,conint
from datetime import datetime
from typing import Optional, Annotated


class PostBase(BaseModel):
    title: str
    content: str
    published:bool = True

class PostCreat(PostBase):
    pass



class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id: int
    email:str


    class Config:
        orm_model = True


class UserLogin(BaseModel):
    email: EmailStr
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str] = None



class Post(PostBase):
    id: int
    created_at: datetime
    owner_id:int
    owner:UserResponse

    class Config:
        orm_model = True

class Vote(BaseModel):
    post_id:int
    direction:Annotated[int,conint(le=1)]


class PostVote(BaseModel):
    Post: Post
    votes:int

    class config:
        orm_model = True