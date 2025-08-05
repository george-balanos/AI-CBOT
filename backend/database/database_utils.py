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
        # connection.close()
        pass
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
        # connection.close()
        pass
    return results


if __name__ == "__main__":
    db_name = "chatbot.db"
    connection = create_database(db_name)

    # Create users table
    users_columns = {
        "user_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "username": "TEXT NOT NULL UNIQUE"
    }
    users_sql = create_table("users", users_columns)
    execute_sql_command(connection, users_sql)

    # Create user_message_history table with foreign key constraint
    message_columns = {
        "message_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "user_id": "INTEGER NOT NULL",
        "sender": "TEXT NOT NULL",
        "message": "TEXT NOT NULL",
        "timestamp": "DATETIME DEFAULT CURRENT_TIMESTAMP",
        "": "FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE"
    }

    message_sql = create_table("user_message_history", message_columns)
    execute_sql_command(connection, message_sql)

    connection.close()

