import sqlite3

DATABASE_PATH = "data/chemai.db"


def get_all_compounds():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, smiles
        FROM compounds
        WHERE smiles != ''
    """)

    data = cursor.fetchall()

    conn.close()

    return data