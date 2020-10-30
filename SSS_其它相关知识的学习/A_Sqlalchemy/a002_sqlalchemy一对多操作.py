from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

HOST='127.0.0.1'
PORT=3306
DATABASE="for_sqlalchemy"
USER='root'
PASSWORD='pengdan'

db_url = 'mysql+mysqlconnector://%s:%s@%s:%d/%s'%(USER,PASSWORD,HOST,PORT,DATABASE)

engine = create_engine(db_url)
DB = sessionmaker(bind=engine)
cli_session = DB()
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), default='游客')

    # articles = relationship("Article") #可以在主表这,也可以在从表那里rela...
    # articles = relationship('Article', uselist=False)#这是一对一双向表
    def __repr__(self):
        return self.username

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)
    content = Column(Text, nullable=True)
    price = Column(Float, default=5.20)
    #
    author_id = Column(Integer, ForeignKey('user.id', ondelete='RESTRICT'))
    # author = relationship('User', backref='articles', uselist=False) #这是一对一,双向表
    author = relationship('User', backref='articles')
    #backref 就是反关联的意思，反向引用，
    #article 通过 author 这个关键字 正向引用 user表中的字段,
    #user 通过 articles 反向引用 article表中的字段


    def __repr__(self):
        return self.title


# 创建数据库
# Base.metadata.drop_all(engine)#
# Base.metadata.create_all(engine)#



# # # # ### 增加数据 ###
# # # # # user = User(username='huang')
# # # # # cli_session.add(user)
# # # # # cli_session.commit()
# # # # #
# # # # # article = Article(title='python从入门到入土',content='test',author_id=1)
# # # # # cli_session.add(article)
# # # # # cli_session.commit()
# # # #
# # # # #通过article表查询作者的信息
# # # # article = cli_session.query(Article).first()
# # # # authorId = article.author_id
# # # # user = cli_session.query(User).get(authorId)
# # # # print(user, ':', user.id)
# # #
# # # #有没有更简便的?
# # # # 前面那个relationship的设置还记得不
# # # article = cli_session.query(Article).first()
# # # user = article.author
# # # print(user, ':', user.id)
# #
# # # 通过user查询article (反向)
# # user = cli_session.query(User).first()
# # articles = user.articles
# # print(articles)
# # #[<__main__.Article object at 0x00000170FA625E20>]#未设置def __repr__
# # #[python从入门到入土] #设置了 def __repr__(self)之后
# #
# # #是个结果列表,文章只有一个作者,作者却可以写多篇文章嘛
# # res = articles[0]
# # print(res)
#
# ### 连表操作:改 ###
# art = cli_session.query(Article).first()
# art.author.username = 'pengdan'
# cli_session.commit()
#
# art = cli_session.query(Article).first()
# print(art.author.username)
# user = cli_session.query(User).first()
# print(user.username)

# 其它操作以此类推啊

cli_session.close()