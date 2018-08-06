from database_connect import connection_handler
from datetime import datetime
import crypt


@connection_handler
def register(cursor, user_name, password):
    cursor.execute("""
                    SELECT EXISTS (SELECT user_name FROM users_table WHERE user_name = %(username)s);
                    """,
                   {'username':username})
    is_already_in_use = cursor.fetchone()
    print(is_already_in_use)
    if is_already_in_use['exists']:
        return 'username already exists'

    cursor.execute


@connection_handler
def get_password_by_username(cusor)