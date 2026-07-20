import sqlite3
import hashlib
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "chemai.db")


def connect():
    return sqlite3.connect(DB_PATH)


def initialize_users():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        email TEXT UNIQUE,

        password TEXT,

        joined TEXT

    )

    """)

    conn.commit()
    conn.close()
    
def initialize_recent_searches():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recent_searches (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT NOT NULL,

        compound TEXT NOT NULL,

        searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


def create_user(username, email, password):

    conn = connect()
    cursor = conn.cursor()

    try:

        cursor.execute(

            """

            INSERT INTO users

            (username,email,password,joined)

            VALUES (?,?,?,?)

            """,

            (

                username,

                email,

                hash_password(password),

                datetime.now().strftime("%Y-%m-%d")

            )

        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def login_user(email, password):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT *

        FROM users

        WHERE (email=? OR username=?)

        AND password=?

        """,

        (

            email,
            
            email,

            hash_password(password)

        )

    )

    user = cursor.fetchone()

    conn.close()

    return user
def initialize_favorites():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS favorites(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        compound TEXT,

        saved_at TEXT

    )

    """)

    conn.commit()
    conn.close()


def save_favorite(username, compound):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT id

        FROM favorites

        WHERE username=?

        AND LOWER(compound)=LOWER(?)

        """,

        (username, compound)

    )

    exists = cursor.fetchone()

    if not exists:

        cursor.execute(

            """

            INSERT INTO favorites

            (username, compound, saved_at)

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
def remove_favorite(username, compound):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(

        """

        DELETE FROM favorites

        WHERE username=?

        AND compound=?

        """,

        (username, compound)

    )

    conn.commit()

    conn.close()
def get_favorites(username):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT compound

        FROM favorites

        WHERE username=?

        ORDER BY id DESC

        """,

        (username,)

    )

    favorites = cursor.fetchall()

    conn.close()

    return favorites