from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


class UserIn(BaseModel):#填入
    username:str
    password:str
    email:EmailStr
    full_name:str=None

class UserOut(BaseModel):#响应
    username:str
    email:EmailStr
    full_name:str=None


#
@app.post('/user/', response_model=UserOut)
async def create_user(*, user:UserIn):
    #response_model会对数据进行过滤再响应
    return user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)