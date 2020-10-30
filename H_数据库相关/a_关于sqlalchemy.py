from H_数据库相关.models import get_db_session, Books

cli_session = next(get_db_session())

cli_session.add(Books(bookname='huangisthebest!'))
cli_session.commit()


obj = cli_session.query(Books).all()


print(obj[0])
