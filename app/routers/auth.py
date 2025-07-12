from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.orm import Session
router = APIRouter(tags=['authentication'])
from .. database import get_db
from .. import schemas, models,utils
from . import auth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


@router.post('/login',response_model=schemas.Token)

def login(user_credential:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user isnt there. sign up first')
    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    

    access_token = auth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token, "token_type":"bearer"}