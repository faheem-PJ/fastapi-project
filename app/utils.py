from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

def hashed_password(p:str):
    hash_pass = pwd_context.hash(p)
    return hash_pass


def verify(plain_password, hash_password):
    return pwd_context.verify(plain_password,hash_password)