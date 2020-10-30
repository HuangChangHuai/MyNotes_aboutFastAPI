from fastapi import FastAPI, Header
from typing import List

app = FastAPI()


@app.get('/items/')
async def read_item(*, user_agent:str = Header(None), users_agent:str=Header(None)):
    return {'User-Agent1':user_agent}, {'test':user_agent},{'UserS_Agent':users_agent}
    #User_Agent1,test的user_agent会被程序认为你要拿的是request种的User_Agent,
    #当你想自己上传时,设置user_agent值是没有用的,要改用其它key,就比如改个users_agent


@app.get('/items2/')
async def read_item2(x_token: List[str] = Header(None)):
    return {'x-token vallues': x_token}





if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
