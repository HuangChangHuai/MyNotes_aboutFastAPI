from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy import String, Column, Integer, Boolean

#这行代码初始化创建了Engine，Engine内部维护了一个Pool（连接池）和Dialect（方言），
# 方言来识别具体连接数据库种类
engine = create_engine(
    'mysql+mysqlconnector://root:pengdan@127.0.0.1:3306/for_sqlalchemy?charset=utf8',
    encoding='utf8',
    #echo=True,#设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
    pool_size=8, #pool数量, defualt 5
    pool_recycle = 60*30 #设置时间以限制数据库多久没连接自动断开
)



from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
#declarative_base()是sqlalchemy内部封装的一个方法，通过其构造一个基类，
# 这个基类和它的子类，可以将Python类和数据库表关联映射起来。

#
class Student(Base):
    __tablename__ = "Students"#
    #数据库表模型类通过__tablename__和表关联起来，Column表示数据表的列。

    uid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False,unique=True, index=True)
    email = Column(String(32), nullable=True,)
    password:str = Column(String(64))
    is_login = Column(Boolean, default=False)
    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(self, *args, **kwargs)

    def __repr__(self):
        return "<Student> {} : {}".format(self.name, self.uid)

    def jiami(self):
        import hashlib
        if not self.password.startswith('md5_'):
            self.password = 'md5_'+hashlib.md5(self.password.encode('utf8')).hexdigest()
            print(self.password)

#创建表，如果存在则忽略
Base.metadata.create_all(engine)

#通过sessionmaker调用创建一个工厂，
# 并关联Engine以确保每个session都可以使用该Engine连接资源：
Db_session = sessionmaker(bind=engine)
cli_session = Db_session()
'''
cli_session 功能性的操作方法包括：
    flush：预提交，提交到数据库文件，还未写入数据库文件中
    commit：提交了一个事务
    rollback：回滚
    close：关闭
'''





'''增
add()
    --将会把Model加入当前cli_session维护的持久空间(cli_session.dirty看到)中，
直到commit时提交到数据库。
    --在add之后执行cli_session.flush()，就可在cli_session中get到对象的属性。


批量插入共有以下几种方法，对它们的批量做了比较，分别是：
    --cli_session.add_all() < bulk_save_object()\
     < bulk_insert_mappings() < SQLAlchemy_core()
'''
# #  #新增数据
# stu_a = Student(name='hahaha', email='210@qq.com', password='huangisthebest')
# stu_a.jiami()
# # #
# cli_session.add(stu_a)
# cli_session.commit()
#
#


#
'''查

filter_by()
    --cli_session.query(Student).filter_by(id=1)[0]

filter()
    --cli_session.query(Student).filter(Student.id==1)[0]

first()
    ...
#last() #应该有, 没有,这个方法没有的,
    ...
all()
    ...
    

'''

# #查找数据
# result = cli_session.query(Student).filter(Student.name=='huang')[0]
# res = cli_session.query(Student).all()
# print(res)
# print(result.name, result.email)

#res = cli_session.query(Student).filter_by(uid=1)[0]
#print(res.name)


# res_list = cli_session.query(Student)
# for i in res_list:
#     # print('type:', type(i))
#     i.jiami() #如果密码没加密的给他加密
# # cli_session.commit()
#
# alist = cli_session.query(Student).order_by(Student.name)
# for i in alist:
#     print(i.name)
#
# cli_session.commit()#其实这里不是说每做完一个就提交一个,反正你该提交的地方提交就对了




'''改,
方式一:
    --直接获得这个对象后修改然后再commit
方式二:
    update()
        --cli_session.query(Student).first().update({'name':'fuck'})
        

'''

##更新数据(修改数据)
# obj = cli_session.query(Student).first()
# print(obj.name)
# obj.password = 'fuckyou!'
# cli_session.commit()
#
# obj = cli_session.query(Student).filter(Student.uid==1)[0]
# print(type(obj))
# print(obj.name)
# obj.password = 'huangisthebest!!!'
# cli_session.commit()
#
#加密密码
# obj = cli_session.query(Student).filter(Student.uid==1)[0]
# obj.jiami()
# cli_session.commit()



'''删

cli_session.query(Users).filter(Users.name == "test").delete()
cli_session.commit()
#以及:
'''
# #删除数据
# obj = cli_session.query(Student).first()
# print(type(obj))
# cli_session.delete(obj)
# cli_session.commit()



cli_session.close()