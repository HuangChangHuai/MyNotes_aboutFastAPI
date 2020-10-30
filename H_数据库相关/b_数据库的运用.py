from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from H_数据库相关.models import engine,get_db_session, Users

app = FastAPI()


'''   '''
class UserBase(BaseModel):
    username:str
    email:str

class UserCreate(UserBase):
    password:str

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True
'''   '''




####
def db_create_user(db: Session, user:UserCreate):
    hashed_password = 'hashed__'+user.password
    db_user_obj = Users(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user_obj)
    db.commit()
    db.refresh(db_user_obj)#刷新
    return db_user_obj

#注册用户
@app.post('/users', response_model=User)
async def regirster(user: UserCreate, db: Session = Depends(get_db_session)):
    return db_create_user(db=db, user=user)#获得db_user_obj,按User的形式返回
####





def get_user(db:Session, user_id:int):
    obj = db.query(Users).filter(Users.id==user_id)[0]
    print(obj)
    return obj


@app.get('/{user_id}', response_model=User)
async def getUser(user_id:int, db:Session = Depends(get_db_session)):
    db_user = get_user(db, user_id=user_id)
    return db_user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)