from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

@app.get('/items/')
async def read_items(username:str=Query(None, min_length=3, max_length=16)):
    #如果写...而不是None的话,就成了必填项了,...表示什么也没有,None表示这里有个None,所以是选填了

    if username:
        return {'user': username}
    else:
        return {'user':'游客'}


#带正则表达式的:
@app.get('/items2/')
async def read_items2(username:str=Query(None, min_length=3, max_length=16, regex='^huang')):#以huang为开头
    #如果写...而不是None的话,就成了必填项了,...表示什么也没有,None表示这里有个None,所以是选填了

    if username:
        return {'user': username}
    else:
        return {'user':'游客'}


#列表:#http://127.0.0.1:8000/items3/?username=huang&username=chang&username=huai
@app.get('/items3/')
async def read_items3(username:List[str]=Query(['huang','chang', 'huai'])):#列表里面是str
    #这列表只是说默认有三个选项而已的,你可以手动添加,只要是字符串就行了,
    #什么都不写的时候就默认这三个
    if username:
        return {'user': username}
    else:
        return {'user':'游客'}



#弃用:
@app.get('/items4/')
async def read_items4(username:str=Query(
    None, 
    min_length=3, 
    max_length=16, 
    regex='^huang',
    deprecated=True,#弃用(就是在前端的时候禁止使用)
    )):

    if username:
        return {'user': username}
    else:
        return {'user':'游客'}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)