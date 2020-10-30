from fastapi import FastAPI, Cookie
from typing import Optional
import uvicorn

'''Cookie要在postman的headers里面设置才能测试:
    key  ----- value
    Cookie     ids_id=1;name=xxxxx;...
'''

app = FastAPI()

@app.get('/items/')
async def read_items(*, ads_id:Optional[str] =Cookie(None)):
    print(ads_id)
    return {'ads_id':ads_id}


if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
