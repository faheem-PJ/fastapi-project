from jose import JWTError, jwt
from datetime import datetime,timedelta
from fastapi import HTTPException,status, Depends
from .. import schemas, database,models
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')
from sqlalchemy.orm import Session
from ..config import settings
#secret key
#algo
#expiration time

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data:dict):
    to_encode = data.copy()


    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expires})

    encoded_token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_token

def verify_access_token(token:str, credential_exeption):

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id = str(payload.get("user_id"))

        if id is None:
            raise credential_exeption
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credential_exeption
    
    return token_data

def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(database.get_db)):
    credential_exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="couldnt authenticate", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credential_exeption)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user