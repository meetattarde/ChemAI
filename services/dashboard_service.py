import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "chemai.db")


def connect():
    return sqlite3.connect(DB_PATH)


def get_dashboard(username):

    conn = connect()
    cur = conn.cursor()

    # Total Searches
    cur.execute(
        "SELECT COUNT(*) FROM search_history WHERE username=?",
        (username,)
    )
    searches = cur.fetchone()[0]

    # Unique Compounds
    cur.execute(
        "SELECT COUNT(DISTINCT compound) FROM search_history WHERE username=?",
        (username,)
    )
    explored = cur.fetchone()[0]

    # Favorites
    cur.execute(
        "SELECT COUNT(*) FROM favorites WHERE username=?",
        (username,)
    )
    favorites = cur.fetchone()[0]

    conn.close()

    return {

        "searches": searches,

        "explored": explored,

        "favorites": favorites,

        "progress": min(explored * 5, 100)

    }