from datetime import datetime, time, timedelta
from uuid import UUID
from uuid import uuid4

from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()


#1
@app.put('/items/{item_id}')
async def read_items(
    item_id:UUID, #这是其它的数据类型把?
    start_datetime:datetime = Body(None),#datetime这些不也是其它的数据类型把?
    end_datetime:datetime = Body(None),#...
    repeat_at:time = Body(None),
    process_after:timedelta = Body(None),):

    return {
        'item_id':item_id,
        'start_datetime': start_datetime,
        'end_datetime': end_datetime,
        'repeat_at': repeat_at,
        'process_after': process_after,
        'start_process': start_datetime+process_after,
        'duration':end_datetime - (start_datetime+process_after)
    }


#2 (在调用时会比1方便)
class Item(BaseModel):
    start_datetime:datetime
    end_datetime:datetime
    repeat_at: time
    process_after: timedelta
    #
    start_process:str
    duration:str

@app.put('/items2/{item_id}')
async def read_items2(item_id: UUID, item:Item):
    item.start_process = item.start_datetime+item.process_after
    item.duration = item.end_datetime -item.start_process
    return {'item_id': item_id, 'item':item}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)