from typing import List
from starlette.requests import Request
from fastapi import FastAPI, File
from starlette.templating import Jinja2Templates
import uvicorn

app = FastAPI()
template = Jinja2Templates(directory='templates')

@app.get('/')
async def index(request:Request):
    return template.TemplateResponse(
        'form_for_upload.html',
        context={
            'request':request,
        }
    )

# @app.post('/files/')
# async def create_file(request:Request, file1:bytes=File(...)):
#     return {'request':request,'file_size':len(file1)}


@app.post('/files/')
async def create_many_files(file1: List[bytes] = File(...)):
    return {
        'message': [len(i) for i in file1],
    }



if __name__ == '__main__':
    uvicorn.run(app=app,host='127.0.0.1', port=8000)