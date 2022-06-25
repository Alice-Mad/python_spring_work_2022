import psycopg


class DB:
    # Класс содержит методы get_connect и сlose_connect
    def __init__(self):
        self.dbname = "postgres"
        self.host = "localhost"
        self.user = "postgres"
        self.password = "mercury1960"

    def get_connect(self):
        conn = psycopg.connect(f"dbname={self.dbname} user={self.user} host={self.host} password={self.password}")
        return conn
