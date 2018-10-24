import connection

@connection.connection_handler
def new_word(cursor, magyar, angol):
    asdf = cursor.execute("""
                      INSERT INTO szotar (magyar, angol)  
                      VALUES (%(magyar)s, %(angol)s);""",
                   {'magyar': magyar,
                    'angol' : angol})


@connection.connection_handler
def list_words(cursor):
    cursor.execute("""
                      SELECT DISTINCT * FROM szotar""")
    return cursor.fetchall()


@connection.connection_handler
def list_words_hungarian_asc(cursor):
    cursor.execute("""
                      SELECT DISTINCT * FROM szotar ORDER BY magyar ASC""")
    return cursor.fetchall()


@connection.connection_handler
def list_words_hungarian_desc(cursor):
    cursor.execute("""
                      SELECT DISTINCT * FROM szotar ORDER BY magyar DESC""")
    return cursor.fetchall()


@connection.connection_handler
def list_words_english_asc(cursor):
    cursor.execute("""
                      SELECT DISTINCT * FROM szotar ORDER BY angol ASC""")
    return cursor.fetchall()


@connection.connection_handler
def list_words_english_desc(cursor):
    cursor.execute("""
                      SELECT DISTINCT * FROM szotar ORDER BY angol DESC""")
    return cursor.fetchall()


@connection.connection_handler
def delete_word_by_id(cursor, id):
    cursor.execute("""
                    DELETE FROM szotar WHERE id = %(id)s;""",
                   {'id': id})
