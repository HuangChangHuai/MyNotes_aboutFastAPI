from fastapi import FastAPI, status
# from starlette import status #上面的status继承自这

app = FastAPI()


#post
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

#get
@app.get("/items2/", status_code=201)
async def create_item2(name: str):
    return {"name": name}

#
@app.post("/items3/", status_code=status.HTTP_404_NOT_FOUND)#不一定写数字,也定义了意思常量
async def create_item3(name: str):
    print('HTTP_404:', status.HTTP_404_NOT_FOUND)
    return {"name": name}

#
@app.get("/i/", status_code=status.HTTP_404_NOT_FOUND)
async def i(name: str):
    print('HTTP_404:', status.HTTP_404_NOT_FOUND)
    return {"name": name}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)