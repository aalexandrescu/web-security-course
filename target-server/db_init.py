import db_connection

def init_db():
    database = ":memory:"

    sql_create_table_users = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        email text NOT NULL                                        
                            ); """
    
    conn = db_connection.create_connection(database)

    # create tables
    if conn is not None:
        # create users table
        db_connection.create_table(conn, sql_create_table_users)

    else:
        print("Error! cannot create the database connection.")
