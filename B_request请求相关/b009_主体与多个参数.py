from fastapi import FastAPI, Path, Body
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name:str
    description: str=None
    price:float
    tax:float=None


#混合参数
@app.put('/items/{item_id}')
async def update_item(*,
    item_id: int=Path(..., title="item的id", ge=10,lt=100),#这是Path,在path上的限制,
    q:str=None, #像get的url参数那种使用的限制是Query
    item:Item=None,):
    result = {'item_id':item_id}
    if q:
        result['q'] = q
    elif item:
        result['item']=item
    return result


class User(BaseModel):
    username:str
    full_name:str=None

#body的特殊参数
@app.put('/items2/{item_id}')
async def test_item(
    *,
    item_id:int,
    item:Item,
    user:User,
    importance:int = Body(...) #这个参数插入到request的body里面去了
):
    result = {'item_id':item_id, 'item':item, 'user':user, 'importance':importance}
    return result    


#嵌入一个单body的参数
@app.put('items3/{item_id}')
async def test_item2(*,
    item_id:int, item:Item=Body(..., embed=True)):
    return {'item_id':item_id, 'item':item}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8001)