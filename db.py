import sqlite3

def init_db():
    conn = sqlite3.connect("tracker.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tracked_items (
            url TEXT PRIMARY KEY,
            title TEXT,
            source TEXT
        )
    """)
    conn.commit()
    conn.close()


def is_new(url, title, source):
    conn = sqlite3.connect("tracker.db")
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM tracked_items WHERE url = ?", (url,))
    exists = cur.fetchone()

    if not exists:
        cur.execute(
            "INSERT INTO tracked_items VALUES (?, ?, ?)",
            (url, title, source)
        )
        conn.commit()
        conn.close()
        return True

    conn.close()
    return False
