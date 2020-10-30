from typing import List
from starlette.requests import Request
from fastapi import FastAPI, File, UploadFile
from starlette.templating import Jinja2Templates
import uvicorn

app = FastAPI()
template = Jinja2Templates(directory='templates')

@app.get('/')
async def index(request:Request):
    return template.TemplateResponse('form_for_upload.html', context={'request':request,})



# @app.post('/files/')
# async def create_UploadFile(file1: UploadFile = File(...)):
#     return {
#         'name': file1.filename,
#         'type': file1.content_type,
#     }


@app.post('/files/')
async def create_UploadFile_list(file1: List[UploadFile] = File(...)):
    return {
        'name': [i.filename for i in file1],
        'type': [i.content_type for i in file1]
    }





if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)