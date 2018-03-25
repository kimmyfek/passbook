from sqlalchemy import create_engine

class SqlAdapter(object):
    def __init__(self, conn_str):
        self.conn_str = conn_str
        self.engine = create_engine(conn_str)

    def fetchall(self, query):
        result = []
        with self.engine.connect() as conn:
            result = conn.execute(query).fetchall()
        return result

    def update(self, query):
        with self.engine.connect() as conn:
            conn.execute(query)
