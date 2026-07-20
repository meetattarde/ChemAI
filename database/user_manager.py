from database.database_manager import get_connection
def add_recent_search(username, compound):

    from datetime import datetime

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS recent_searches(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            compound TEXT,
            searched_at TEXT
        )
        """
    )

    # Remove any existing duplicate (same username and compound, case-insensitive)
    cursor.execute(
        """
        DELETE FROM recent_searches
        WHERE username=?
        AND LOWER(compound)=LOWER(?)
        """,
        (username, compound),
    )

    # Insert new search
    cursor.execute(
        """
        INSERT INTO recent_searches (username, compound, searched_at)
        VALUES (?,?,?)
        """,
        (username, compound, datetime.now().strftime("%Y-%m-%d %H:%M")),
    )

    conn.commit()
    conn.close()
def get_recent_searches(username, limit=5):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT DISTINCT compound

        FROM recent_searches

        WHERE username=?

        ORDER BY id DESC

        LIMIT ?

        """,

        (username, limit)

    )

    searches = cursor.fetchall()

    conn.close()

    return searches

def update_profile(old_username, new_username, new_email):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        UPDATE users

        SET username=?,

            email=?

        WHERE username=?

        """,

        (

            new_username,

            new_email,

            old_username

        )

    )

    conn.commit()

    conn.close()
def update_password(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        UPDATE users

        SET password=?

        WHERE username=?

        """,

        (

            hash_password(password),

            username

        )

    )

    conn.commit()

    conn.close()

def verify_password(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(

        """

        SELECT id

        FROM users

        WHERE username=?

        AND password=?

        """,

        (

            username,

            hash_password(password)

        )

    )

    user = cursor.fetchone()

    conn.close()

    return user is not None