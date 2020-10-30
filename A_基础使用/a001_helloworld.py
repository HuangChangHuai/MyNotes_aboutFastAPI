from fastapi import FastAPI
import aioredis

'''
    http://127.0.0.1:8000/docs
    /docs这个是fastapi自带的自动生成的api文档
'''

app = FastAPI()

@app.get('/')
async def main():
    return {'message':'hello world, this is fastapi'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host='127.0.0.1', port=8000)