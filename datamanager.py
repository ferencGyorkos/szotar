import connection

@connection.connection_handler
def new_word(cursor, magyar, angol):
    asdf = cursor.execute("""
                      INSERT INTO szotar (magyar, angol)  
                      VALUES (%(magyar)s, %(angol)s);""",
                   {'magyar': magyar,
                    'angol' : angol})