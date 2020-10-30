from fastapi import FastAPI, Path, Query
import uvicorn

app = FastAPI()

@app.get('/item/{item_id}')
async def read_items(
    item_id:int = Path(..., title='项目id', ge=50, le=100),#>=50, <=100
    q:str = Query(None, alias='测试内容'), #alias 提示
    size : float = Query(1, gt=0, lt=3.14)):
    return {
        'item_id':item_id,
        'q':q,
        'size':size,
    }






if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)    