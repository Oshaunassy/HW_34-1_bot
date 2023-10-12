GREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        FIRST_NAME CHAR(50),
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )        
"""

CREATE_USER_ANSWER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS users_answers
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        ANSWER CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
"""
INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?, ?, ?, ?, ?)

"""

INSERT_USER_ANSWER_QUERY = """
INSERT OR IGNORE INTO users_answers VALUES (?, ?, ?, ?)
"""