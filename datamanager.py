import connection

@connection.connection_handler
def new_word(cursor, magyar, angol):
    new_word = cursor.execute("""
                      INSERT INTO szotar (magyar, angol)  
                      VALUES (%(magyar)s, %(angol)s);""",
                   {'magyar': magyar,
                    'angol' : angol})