import sqlite3
from datetime import datetime

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "data", "chemai.db")


def connect():

    return sqlite3.connect(DB_PATH)


def initialize_feedback():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS ratings(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        rating INTEGER NOT NULL,

        created_at TEXT

    )

    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS feedback(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT,

        category TEXT,

        message TEXT,

        created_at TEXT

    )

    """)

    conn.commit()

    conn.close()


def save_rating(rating):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO ratings

        (rating, created_at)

        VALUES (?,?)

        """,

        (

            rating,

            datetime.now().strftime("%Y-%m-%d %H:%M")

        )

    )

    conn.commit()

    conn.close()


def save_feedback(

        name,

        email,

        category,

        message

):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        """

        INSERT INTO feedback

        (name,email,category,message,created_at)

        VALUES (?,?,?,?,?)

        """,

        (

            name,

            email,

            category,

            message,

            datetime.now().strftime("%Y-%m-%d %H:%M")

        )

    )

    conn.commit()

    conn.close()


def get_average_rating():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT AVG(rating) FROM ratings"

    )

    avg = cursor.fetchone()[0]

    conn.close()

    return round(avg, 2) if avg else 0


def total_ratings():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM ratings"

    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_feedback():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT

        name,

        email,

        category,

        message,

        created_at

        FROM feedback

        ORDER BY id DESC

        """

    )

    data = cursor.fetchall()

    conn.close()

    return data