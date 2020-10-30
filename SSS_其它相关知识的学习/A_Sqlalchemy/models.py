from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOST='127.0.0.1'
PORT=3306
DATABASE="for_sqlalchemy"
USER='root'
PASSWORD='pengdan'

# db_url = 'sqlite://sqlite.db' # sqlite3
db_url = 'mysql+mysqlconnector://%s:%s@%s:%d/%s?charset=utf8'%(USER,PASSWORD,HOST,PORT,DATABASE)

engine = create_engine(db_url, encoding='utf8')

DB = sessionmaker(bind=engine)





Base = declarative_base()

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
        return '课程:'+self.name


Base.metadata.create_all(engine)