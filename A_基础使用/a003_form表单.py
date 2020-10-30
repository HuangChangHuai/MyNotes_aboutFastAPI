from starlette.requests import Request
from fastapi import FastAPI, Form #新加了一个from
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
template = Jinja2Templates(directory='templates')
app.mount('/static/', StaticFiles(directory='static'), name='static')

@app.get('/')
async def login(request:Request):
    message = '请登录!'
    return template.TemplateResponse('login.html',locals())



@app.post('/user/')
async def create_upload_files(request:Request, username:str=Form(...), password:str=Form(...)):
    print('username', username)
    print('password', password)
    # return template.TemplateResponse('index.html', context={'request':request, 'username':username})
    return template.TemplateResponse('index.html', locals())

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)