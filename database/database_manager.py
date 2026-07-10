import sqlite3

DATABASE = "data/chemai.db"


def connect():
    return sqlite3.connect(DATABASE)


def create_database():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compounds(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT UNIQUE,

        formula TEXT,

        molecular_weight REAL,

        iupac_name TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_compound(name, formula, weight, iupac):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT OR IGNORE INTO compounds
    (name,formula,molecular_weight,iupac_name)

    VALUES(?,?,?,?)

    """, (name, formula, weight, iupac))

    conn.commit()

    conn.close()