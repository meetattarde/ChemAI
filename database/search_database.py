import sqlite3

DATABASE_PATH = "data/chemai.db"


def search_compound(name):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM compounds
        WHERE LOWER(name)=LOWER(?)
        """,
        (name,)
    )

    result = cursor.fetchone()

    conn.close()

    return result