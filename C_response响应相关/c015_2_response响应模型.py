from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name:str
    description:str=None
    price:float
    tax: float=10.4
    tags: List[str] = []

datas = {
    'foo': {'name': 'huai', 'price': 30},
    'huang': {'name':'huangchanghaui', 'description':'a best man', 'price':530, 'tax':10},
    'peng':{'name':'dan', 'description':None, 'price':5, 'tax':1, 'tags':['a','b','c']},
}


#response_model_exclude_unset=True : #数据有啥响应啥
    #意思是数据里有什么就响应什么, 数据里没有的项,也不返回model里面的默认值
@app.get('/datas1/{item}', response_model=Item, response_model_exclude_unset=True)
async def read_item(item: str):
    return datas[item]


#response_model_exclude={'tax',...} : #排除
    #数据里没有的,会返回model里面的默认项,
    #这里则排除掉tax项,不要tax
@app.get('/datas2/{item}', response_model=Item, response_model_exclude={'tax'})
async def read_item2(item: str):
    return datas[item]



#response_model_include=['name','price','tax'] : 只显示这仨
    #数据里多的不显示,只显示这仨,
    #数据里没有的会显示model里的默认值
@app.get('/datas3/{item}', response_model=Item, response_model_include=['name','price','tax'])#include 包含
async def read_item3(item: str):
    return datas[item]



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)