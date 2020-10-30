# -*- coding: UTF-8 -*-
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):#继承了BaseItem
    type = "car"
    


class PlaneItem(BaseItem):#BaseItem
    type = "plane"
    size: int
    test:int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car", 'size':15, 'test':500},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

#response_model=Union[PlaneItem, CarItem]
    #前面的model可以继承,现在又可以联合起来用
    #如果是car,就使用car的类,如果是plane,就使用飞机类
    #比如Car的model没有size,但是Union的plane的model又szie,数据里的item1是属于car的,
        #返回的数值也有 size    
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])#item2例子
async def read_item(item_id: str):
    return items[item_id]
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)