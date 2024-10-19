import sqlite3

class Database:
    def __init__(self, path_to_db='db.sqlite3'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def add_group(self, group_number):
        con = self.connection
        cur = con.cursor()
        max_id = cur.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM groups").fetchone()[0]
        print(max_id)
        sql = """
            INSERT INTO groups (id, group_number) VALUES (?, ?)
        """
        cur.execute(sql, (max_id, group_number))
        if cur:
            con.commit()
        else:
            print('Error')
