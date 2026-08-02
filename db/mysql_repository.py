import mysql.connector
from db.repository import Repository

class MysqlRepository(Repository):
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'langguessr',
            'host': 'localhost',
            'port': 3306,
            'database': 'langguessr'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def load_orthographies(self):
        self.cursor.execute("SELECT name, grapheme FROM orthographies")
        orthographies = {}
        for name, grapheme in self.cursor.fetchall():
            if name not in orthographies:
                orthographies[name] = set()
            orthographies[name].add(grapheme)
        return orthographies