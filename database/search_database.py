import sqlite3
import os

DATABASE_PATH = "data/chemai.db"

print(f"[Search Database] Using database: {os.path.abspath(DATABASE_PATH)}")


def search_compound(name):
    conn = sqlite3.connect(os.path.abspath(DATABASE_PATH))
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