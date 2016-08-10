import sqlite3

def create_database():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    # create a table
    cursor.execute("""CREATE TABLE albums
                          (title text, artist text, release_date text,
                           publisher text, media_type text)
                       """)
    # insert some data
    cursor.execute("INSERT INTO albums VALUES "
                   "('Glow', 'Andy Hunter', '7/24/2012',"
                   "'Xplore Records', 'MP3')")

    # save data to database
    conn.commit()

    # insert multiple records using the more secure "?" method
    albums = [('Exodus', 'Andy Hunter', '7/9/2002',
               'Sparrow Records', 'CD'),
              ('Until We Have Faces', 'Red', '2/1/2011',
               'Essential Records', 'CD'),
              ('The End is Where We Begin', 'Thousand Foot Krutch',
               '4/17/2012', 'TFKmusic', 'CD'),
              ('The Good Life', 'Trip Lee', '4/10/2012',
               'Reach Records', 'CD')]
    cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)",
                       albums)
    conn.commit()

def delete_artist(artist):
    """
    Delete an artist from the database
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    sql = """
    DELETE FROM albums
    WHERE artist = ?
    """
    cursor.execute(sql, [(artist)])
    conn.commit()
    cursor.close()
    conn.close()


def update_artist(artist, new_name):
    """
    Update the artist name
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    sql = """
    UPDATE albums
    SET artist = ?
    WHERE artist = ?
    """
    cursor.execute(sql, (new_name, artist))
    conn.commit()
    cursor.close()
    conn.close()


def select_all_albums(artist):
    """
    Query the database for all the albums by a particular artist
    """
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    sql = "SELECT * FROM albums WHERE artist=?"
    cursor.execute(sql, [(artist)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    import os
    if not os.path.exists("mydatabase.db"):
        create_database()

    delete_artist('Andy Hunter')
    update_artist('Red', 'Redder')
    print(select_all_albums('Thousand Foot Krutch'))