import sqlite3
from database import sql_queries

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.GREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_ANSWER_TABLE_QUERY)

        self.connection.commit()

    def sql_insert_user_query(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
        sql_queries.INSERT_USER_QUERY,
        (None, telegram_id, username, first_name, last_name,
    ))
        self.connection.commit()

    def sql_insert_user_answer_query(self, telegram_id, username, answer):
        self.cursor.execute(
            sql_queries.INSERT_USER_ANSWER_QUERY,
            (None, telegram_id, username, answer)
        )
        self.connection.commit()