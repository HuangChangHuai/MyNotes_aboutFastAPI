from starlette.requests import Request
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static/', StaticFiles(directory='static'), name='static')
#name是为了在html{{ url_for('static', path='xxxx') }},
#将来这里或者目录的路径怎么改都好,html那里就不用改了;
#path是以static为父目录的相对路径

@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse('index.html',{'request':request, 'message':'hello world!'})

@app.get('/{name}/')
async def user(request:Request, name:str):
    return templates.TemplateResponse('index.html', context={'request':request, 'message':name}, status_code=200)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)