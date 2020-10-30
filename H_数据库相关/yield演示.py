from H_数据库相关.models import engine, sessionmaker, Books


def get_db():
    try:
        db = sessionmaker(bind=engine)()
        yield db
    finally:
        db.close() #无论报没报错,反正就db都关闭

cli = next(get_db())

print(cli.query(Books).first().bookname)