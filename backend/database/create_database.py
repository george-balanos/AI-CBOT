import sqlite3

def create_database(db_name):
    connection = sqlite3.connect(db_name)
    return connection

def create_cursor(connection):
    cursor = connection.cursor()
    return cursor

def create_table(table_name, table_columns):

    sql_command = f"CREATE TABLE {table_name} ("

    for column in table_columns:
        sql_command += f"{column} {table_columns[column]}, "
    
    sql_command = sql_command.strip()[:-1]
    sql_command += ")"

    return sql_command

def execute_sql_command(connection, sql_command, values=None):

    cursor = create_cursor(connection)

    if values:
        cursor.execute(sql_command, values)
    else:
        cursor.execute(sql_command)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    pass

    # connection = create_database("chatbot.db")

    # columns = {
    #     "user_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    #     "username": "TEXT NOT NULL UNIQUE"
    # }

    # command = create_table("users", columns)
    # execute_sql_command(connection, command)

    # command = """INSERT INTO users (username) VALUES (?)"""
    # values = ["George"]
    # execute_sql_command(connection, command, values)

    # con = sqlite3.connect("chatbot.db")
    
    # cur = con.cursor()
    # cur.execute(
    #     """CREATE TABLE users(
    #         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         username TEXT NOT NULL UNIQUE
    #     )"""
    # )

    # cur.execute("""
    #     INSERT INTO users (username) VALUES (?)
    # """, ("George",))

    # con.commit()

    # res = cur.execute("SELECT * FROM users")
    # print(res.fetchall())