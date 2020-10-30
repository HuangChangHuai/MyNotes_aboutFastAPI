from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOST='127.0.0.1'
PORT=3306
DATABASE="for_fastapi"
USER='root'
PASSWORD='pengdan'

db_url = 'sqlite:///sqlite3.db'  #sqlite数据库
# db_url = 'mysql+mysqlconnector://%s:%s@%s:%d/%s?charset=utf8'%(USER,PASSWORD,HOST,PORT,DATABASE)

engine = create_engine(db_url, encoding='utf8')

def get_db_session():
    try:
        db_cli = sessionmaker(bind=engine)()
        yield db_cli
    finally:
        db_cli.close()
        print('此次连接查询完成,已断开')





Base = declarative_base()
'''
class GUOJIA(Base):
    __tablename__ = 'GUOJIA'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16),default='中国')
    def __repr__(self):
        return "国家:"+self.name

class Qiangxie(Base):
    __tablename__ = 'Qiangxie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16), nullable=False)
    GUOJIA_id = Column(Integer, ForeignKey('GUOJIA.id', ondelete='RESTRICT'))
    GUOJIA = relationship("GUOJIA", backref='Qiangxie')
    def __repr__(self):
        return '枪械:'+self.name
'''

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bookname = Column(String(64), nullable=False, unique=True, index=True)

    def __repr__(self):
        return self.bookname


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(32), nullable=True, )
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    def __repr__(self):
        return self.username+' -> '+self.email




Base.metadata.create_all(engine)