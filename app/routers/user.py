from fastapi import  status,HTTPException, Depends, APIRouter 
from . . import models,schemas, utils
from sqlalchemy.orm import Session
from . . database import get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
)



@router.post("/",response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
    
    hashed_password = utils.hashed_password(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    
    return new_user


@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Lok pai ni")
    

    return user