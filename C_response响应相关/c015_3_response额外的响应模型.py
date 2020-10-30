from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)
db_obj = redis.Redis(connection_pool=pool)

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str=None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str=None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str=None

def 加密密码(raw_password:str):
    import hashlib
    return hashlib.md5(raw_password.encode('utf8')).hexdigest()

def fake_save_user(user_in: UserIn):
    hashed_password = 加密密码(user_in.password)
    #
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)#
    #

    db_obj.setex('password', 1800, hashed_password)
    
    return user_in_db


@app.post('/user/', response_model=UserOut)
async def create_user(*, user_in:UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
    db_obj.close()