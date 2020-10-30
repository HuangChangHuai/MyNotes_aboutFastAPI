from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')#相当于/token

class UserModel(BaseModel):
    username:str
    password:str
    email: str

def test_token(token):
    return UserModel(
        username=token+'|test_token',
        password='test',
        email='test'
    )

async def get_cur_user(token:str=Depends(oauth2_scheme)):
    return test_token(token)

@app.get('/')
async def index(cur_user: UserModel = Depends(get_cur_user)):
    return cur_user
'''在postman, url输入 127.0.0.1:8000
在body里添加key-value进行测试: 
    key ------------------value
    Authorization        bearer huang (bearer不能没有)
'''

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)