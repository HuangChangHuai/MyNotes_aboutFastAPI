from fastapi import FastAPI

#body传参
from pydantic import BaseModel


app = FastAPI()

#url传参
@app.get('/user/huang')
async def userhuang():
    return {'name':'huang'}

@app.get('/user/{text}')
#这个泛匹配的一定要在前面那种具体的后面, 不然像前面那个具体的会被泛匹配的抢走
async def usertext(text:str):
    return {'result':text}

#''''''


#枚举参数列表
'''好处呢就是在这个路径下,如果没有符合其它的匹配的话,必须要符合Name里的'''
from enum import Enum

class Name(str, Enum):
    patch = 'huang'
    put = 'huai'
    delete = 'peng'

@app.get('/test/{how}')
async def meiju(how: Name):
    if how == Name.patch:
        return {'how':how, 'message':'adsgasdgaag'}
    elif how.value == 'huai':
        return 'Yeah!'
    return {'how': how, 'message':'fuck!'}

#''''''


# query_params (get方式那种呢)#query传参
@app.get('/query_params/')
async def art_list(page:int=1, limit:int=10):
    return {'page': page, 'limit': limit}


#复合传参
#http://127.0.0.1:8000/haha/huangchanghaui?code=100&SS=50
@app.get('/haha/{test}')
async def testest(test:str, code:int=404, SS:int=0):
    return {'name':test,'code':code, 'ss':SS}



class Item(BaseModel):
    name:str
    description:str = None
    price:float
    tax:float=None
@app.post('/item/')
async def create_item(item:Item):
    print(item.dict())
    return item,'666'
@app.put('/items/{item_id}')
async def create_item2(item_id:int, item:Item, q:str=None):
    result = {'item_id':item_id, **item.dict()}
    if q: result.update({'q':q})
    print(result)
    return result



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)