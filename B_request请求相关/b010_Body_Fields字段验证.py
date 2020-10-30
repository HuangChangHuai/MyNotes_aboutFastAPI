from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name:str
    description:str = Field(None, title='描述', max_lenth=16)
    price :float = Field(..., gt=0, description="大于0")
    tax: float = None

@app.put('/items/{item_id}')
async def update_item1(*,
    item_id:int, item:Item=Body(..., embed=True)): #给提交的数据进行校验的
    return {'item_id':item_id, 'item':item}


@app.put('/items2/{item_id}')
async def update_item2(*,
    item_id:int,
    item:Item=Body(...,
                  example = { #默认例子数据
                  'name': 'huang',
                  'description': 'huang is the best!',
                  'price':0,
                  'fuck': 520,
                })):
    return {'item_id':item_id, 'item':item}



if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)