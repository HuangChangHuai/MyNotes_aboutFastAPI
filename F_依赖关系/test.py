from fastapi import FastAPI, Depends
import uvicorn


app = FastAPI()


class GetObj:
    def __init__(self, id:int=1, name:str='huang'):
        self.id = id
        self.name = name


@app.get('/')
# async def index(obj:GetObj =Depends(GetObj)):
async def index(obj:GetObj =Depends()): #少写了个GetObj
    #Depends的GetObj参数使用url query param (就是get方法传参)的方式
    if obj.id:
        if obj.id == 1:
            obj.name = '管理员:'+obj.name
        else:
            obj.name = '用户:'+obj.name
        return {'id':obj.id, 'name':obj.name}
    else:
        return {'message':'fuck!'}

@app.post('/test/') #在post里也是使用url query param的方式
async def index2(obj:GetObj =Depends(GetObj)):
    #Depends的GetObj参数使用url query param (就是get方法传参)的方式
    if obj.id:
        if obj.id == 1:
            obj.name = '管理员:'+obj.name
        else:
            obj.name = '用户:'+obj.name
        return {'id':obj.id, 'name':obj.name}
    else:
        return {'message':'fuck!'}



def func(name:str=None, age:int=0):
    return {'name':name, 'age':age}

#http://127.0.0.1:8000/test2/?name=huangchanghuai&age=3000
@app.get('/test2/')
async def index3(obj:dict = Depends(func)):
    print(obj)
    return obj


## ##
def test5(name2:str=''):
    print(name2)
    return {'name2':name2}

def test4(name1:str='', obj2:dict= Depends(test5)):
    print(name1)
    print(obj2)
    return {'name1':name1, 'obj2':obj2}
#子依赖
@app.get('/test3/')
async def index4(obj:dict = Depends(test4)):
    return obj
#http://127.0.0.1:8000/test3/?name1=huang&name2=peng





@app.get('/test4/', dependencies=[Depends(test4), Depends(func)])
async def index5():
    #这个呢与之前那些一样执行了依赖关系,但是它们返回的值(返不返回也不用)则不会传给操
    # 作函数了,但是raise 引发该报错还是会报错的
    #http://127.0.0.1:8000/test4/?name1=huang1&name2=chang2&name=huai0&age=18
    return 'fuck!'





if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)