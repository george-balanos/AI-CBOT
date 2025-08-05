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
    try:
        if values:
            result = cursor.execute(sql_command, values)
        else:
            result = cursor.execute(sql_command)
        connection.commit()
    finally:
        connection.close()
    return result

def execute_sql_query(connection, sql_query, values=None):
    cursor = create_cursor(connection)
    try:
        if values:
            cursor.execute(sql_query, values)
        else:
            cursor.execute(sql_query)
        results = cursor.fetchall()
    finally:
        connection.close()
    return results




if __name__ == "__main__":
    # pass

    # # Create database
    # create_database("chatbot.db")

    # # Create Table: users

    # connection = create_database("chatbot.db")

    # columns = {
    #     "user_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    #     "username": "TEXT NOT NULL UNIQUE"
    # }

    # sql_command = create_table("users", columns)
    # execute_sql_command(connection, sql_command)

    # Create Table: user_message_history

    connection = create_database("chatbot.db")

    columns = {
        "message_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "user_id": "INTEGER NOT NULL",
        "sender": "TEXT NOT NULL",  # 'user' or 'bot'
        "message": "TEXT NOT NULL",
        "timestamp": "DATETIME DEFAULT CURRENT_TIMESTAMP",
        "": "FOREIGN KEY(user_id) REFERENCES users(user_id)"
    }

    sql_command = create_table("user_message_history", columns)
    execute_sql_command(connection, sql_command)

