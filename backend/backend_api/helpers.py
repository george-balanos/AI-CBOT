from ..database import database_utils

def login_user(username):
    
    connection = database_utils.create_database("./backend/database/chatbot.db")
    
    check_query = "SELECT username FROM users WHERE username = ?"
    existing_user = database_utils.execute_sql_query(connection=connection, sql_query=check_query, values=[username])

    if not existing_user:
        connection = database_utils.create_database("./backend/database/chatbot.db")
        command = f"""INSERT INTO users (username) VALUES (?)"""
        value = [username]

        database_utils.execute_sql_command(connection=connection, sql_command=command, values=value)

        add_message(username, "You are a helpful AI chat bot. Your name is AI-CBOT!", "system")

def get_user_id(username):
    connection = database_utils.create_database("./backend/database/chatbot.db")

    get_user_id_query = "SELECT user_id FROM users WHERE username = ?"
    result = database_utils.execute_sql_query(connection, get_user_id_query, [username])

    if not result:
        print(f"User {username} not found.")
        return
    
    return result[0][0]

def add_message(username, message, sender):

    user_id = get_user_id(username)
    
    connection = database_utils.create_database("./backend/database/chatbot.db")

    insert_message_query = "INSERT INTO user_message_history (user_id, sender, message) VALUES (?, ?, ?)"
    values = [user_id, sender, message]
    database_utils.execute_sql_command(connection, insert_message_query, values)

def get_all_user_messages(username):

    user_id = get_user_id(username)

    connection = database_utils.create_database("./backend/database/chatbot.db")

    get_all_messages_query = "SELECT sender, message, timestamp FROM user_message_history WHERE user_id = ?"
    value = [user_id]

    result = database_utils.execute_sql_query(connection, get_all_messages_query, value)

    messages = [
        {"sender": row[0], "message": row[1], "timestamp": row[2]} 
        for row in result
    ]

    return messages


if __name__ == "__main__":

    add_message("George", "Hello, World!", "bot")

    print(get_all_user_messages("George"))