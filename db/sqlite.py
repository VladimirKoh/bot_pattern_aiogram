import sqlite3

import logging


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()


    def create_table(self):
        try:
            with self.connection:
                return self.cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id VARCHAR(20) UNIQUE PRIMARY KEY, user_name VARCHAR(40))")
        except Exception as e:
            logging.exception(e)


    def add_user(self, user_id: str, user_name: str):
        try:
            with self.connection:
                return self.cursor.execute("INSERT INTO users (user_id, user_name) VALUES(?, ?)", (user_id, user_name, ))
        except Exception as e:
            logging.exception(e)
        

    def exist_user(self, user_id):
        try:
            with self.connection:
                result = self.cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}").fetchall()
                return bool(len(result))
        except Exception as e:
            logging.exception(e)

