# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
# from pydantic import BaseModel
#
# # 模拟用户数据（模拟）
# fake_users_db = {
#     "huang": {
#         "username": "huang",
#         "full_name": "huang Doe",
#         "email": "huang@example.com",
#         "hashed_password": "fakehashedpengdan",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "hashed_password": "fakehashedsecret2",
#         "disabled": True, # 禁用此用户
#     },
# }
#
# class User(BaseModel):
#     username:str
#     email:str = '21dsg@qq.com'
#     full_name:str = None
#     disabled:bool = None
#
# class UserInDB(User):
#     hashed_password:str
#
#
# app = FastAPI()
#
# def get_user(db, username):
#     '''获取用户的函数'''
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#
# def decode_token(token):
#     '''解码token的函数从数据库获取这名用户并返回'''
#     user = get_user(db=fake_users_db, username=token)
#     return user
#
# oauth2_scheme = OAuth2PasswordBearer('/token')#
#
# async def get_curr_user(token: str= Depends(oauth2_scheme)):
#     '''get/:
#         1:
#             到 oauth2_scheme 那里获取token,
#         2:
#             调用解码函数解码token,获取用户并返回
#     '''
#     user = decode_token(token)
#     if user:
#         return user
#     else:
#         raise HTTPException(
#             status_code=401,
#             detail='找不到这个用户',
#             headers={'WWW-Authenticate':'Bearer'}
#         )
#
#
# ##
# @app.get('/')
# async def index(curr_user: User = Depends(get_curr_user)):
#     '''get/: 到 get_curr_user 那里获取用户并返回'''
#     return curr_user
#
#
#
# def fake_hash_passwd(raw_password):#模拟哈希函数加密密码
#     return "fakehashed" + raw_password
#
# ## 这里接收表单
# @app.post('/token')
# async def login(form_data:OAuth2PasswordRequestForm = Depends()):
#     '''@app.post('/token'):
#         1:
#             从OAuth2PasswordRequestForm里获取表单数据
#         2:
#             用表单数据的username到数据库里找人,找不到就报错
#         3:
#             找到了就把数据实例化到userindb这个模型里去
#         4:
#             把密码哈希, 如果结果一致,则返回账号的token和它的类型
#             这里的token图方便 直接使用了username而已
#     '''
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail='账号或密码错了')
#     else:
#         user = UserInDB(**user_dict)
#         hashed_passwd = fake_hash_passwd(form_data.password)
#         if not hashed_passwd == user.hashed_password:
#             raise HTTPException(status_code=400, detail='账号或密码错了2')
#         else:
#             return {'access_token': user.username, 'token_type':'bearer'}
#
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host='127.0.0.1', port=8000)
#
#


#
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get('/')
# async def index():
#     return {"message": "this is index page information"}
#
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app=app, host='127.0.0.1', port=8000)
#
#




# import fastapi
# import uvicorn
#
# app = fastapi.FastAPI()
#
# @app.get('/')
# async def index():
#     return {'result':200}
#
#
#
# if __name__ == '__main__':
#     uvicorn.run(app=app, host='127.0.0.1', port=8000)
#
#
#























