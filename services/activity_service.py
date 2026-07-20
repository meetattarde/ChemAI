import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "chemai.db")


def connect():
    return sqlite3.connect(DB_PATH)


def initialize_activity():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""

    CREATE TABLE IF NOT EXISTS search_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        compound TEXT,

        searched_at TEXT

    )

    """)

    conn.commit()
    conn.close()


def save_search(username, compound):

    conn = connect()
    cur = conn.cursor()

    cur.execute(

        """

        INSERT INTO search_history

        (username, compound, searched_at)

        VALUES (?,?,?)

        """,

        (

            username,

            compound,

            datetime.now().strftime("%Y-%m-%d %H:%M")

        )

    )

    conn.commit()
    conn.close()


def total_searches(username):

    conn = connect()
    cur = conn.cursor()

    cur.execute(

        """

        SELECT COUNT(*)

        FROM search_history

        WHERE username=?

        """,

        (username,)

    )

    total = cur.fetchone()[0]

    conn.close()

    return total


def explored_compounds(username):

    conn = connect()
    cur = conn.cursor()

    cur.execute(

        """

        SELECT COUNT(DISTINCT compound)

        FROM search_history

        WHERE username=?

        """,

        (username,)

    )

    total = cur.fetchone()[0]

    conn.close()

    return total