import sqlite3
import os

DATABASE_PATH = "data/chemai.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():

    os.makedirs("data", exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compounds (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT UNIQUE,

        formula TEXT,

        molecular_weight REAL,

        iupac_name TEXT,

        smiles TEXT,

        inchikey TEXT,

        pubchem_cid INTEGER,

        last_updated TEXT

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metadata (

        key TEXT PRIMARY KEY,

        value TEXT

    )
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO metadata
    VALUES ('db_version', '2.0')
    """)

    conn.commit()
    conn.close()


def save_compound(data):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO compounds
    (
        name,
        formula,
        molecular_weight,
        iupac_name,
        smiles,
        inchikey,
        pubchem_cid,
        last_updated
    )

    VALUES (?,?,?,?,?,?,?,?)

    """,
    (
        data["name"],
        data["formula"],
        data["molecular_weight"],
        data["iupac_name"],
        data["smiles"],
        data["inchikey"],
        data["pubchem_cid"],
        data["last_updated"]
    ))

    conn.commit()
    conn.close()