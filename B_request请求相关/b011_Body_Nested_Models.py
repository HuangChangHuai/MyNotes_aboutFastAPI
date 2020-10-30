from fastapi import FastAPI
from typing import List, Dict #

from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl #不是url不能通过校验(相对路径不同通过校验)
    name:str

@app.post('/images/test/')
async def create_images(*, images:List[Image]): #
    return images    


@app.post('/key-value')
async def create_key_v(weights: Dict[int, float]):#注意,在前端时json的key是""包住的,即使是int
    return weights





if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)