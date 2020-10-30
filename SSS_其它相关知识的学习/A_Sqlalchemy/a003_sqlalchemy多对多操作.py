from sqlalchemy import Table, create_engine, Column, Integer, String, Float, ForeignKey,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

HOST='127.0.0.1'
PORT=3306
DATABASE="for_sqlalchemy"
USER='root'
PASSWORD='pengdan'

db_url = 'mysql+mysqlconnector://%s:%s@%s:%d/%s?charset=utf8'%(USER,PASSWORD,HOST,PORT,DATABASE)

engine = create_engine(db_url, encoding='utf8')
DB = sessionmaker(bind=engine)
cli_session = DB()
Base = declarative_base()


#一架飞机可以有多个特点
#每个特点都可以包含在多架飞机里


#多对多关系会在两个类之间增加一个关联的表。
#这个关联的表在 relationship() 方法中通过 secondary 参数来表示。
#通常这个表会通过 MetaData 对象来与声明基类关联
#所以这个 ForeignKey 指令会使用链接来定位到远程的表：
#
#创建表映射
feiji_to_tag = Table(
    'feiji_to_tag',
    Base.metadata,
    Column('feiji_id', Integer, ForeignKey('feiji.id')),
    Column('tag_id', Integer, ForeignKey('tag.id')),)


#
class Feiji(Base):
    __tablename__ = 'feiji'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16), nullable=False)
    tags = relationship('Tag', secondary=feiji_to_tag, backref='feiji')

    def __repr__(self):
        return self.name

#
class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16), nullable=False)
    feijis = relationship(
        'Feiji',
        secondary=feiji_to_tag,
        backref='tag')
    def __repr__(self):
        return self.name


# # ## 创建数据库 #这东西用了就要注释掉, 不然数据又被删了
# Base.metadata.drop_all(engine)#
# Base.metadata.create_all(engine)#


# # ## 增加数据
# tag = Tag(name='空优战斗机')
# tag2 = Tag(name='战略轰炸机')
# tag3 = Tag(name='三代机')
# #
# feiji = Feiji(name='F16')
# # #多对多增
# feiji.tags = [tag,tag2,tag3]
#
# cli_session.add_all([tag, tag2, tag3, feiji])
# cli_session.commit()
# #
# # #根据飞机找标签
# # feiji = cli_session.query(Feiji).first()
# # print(feiji, feiji.tags)#F16 [空优战斗机, 战略轰炸机, 三代机]
# # #根据标签找飞机
# # tag = cli_session.query(Tag).first()
# # print(tag, tag.feiji) #空优战斗机 [F16, F22]



cli_session.close()