from sqlalchemy import create_engine, MetaData

# engine = create_engine("mysql+pymysql://root@localhost:3306/project")
engine = create_engine("mysql+pymysql://project:oat41042@127.0.0.1:3306/project")
meta = MetaData()

conn = engine.connect()
