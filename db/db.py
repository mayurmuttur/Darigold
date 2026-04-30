import sqlite3
from pathlib import Path

DB_PATH = Path('darigold.db')
SCHEMA_PATH = Path('db/schema.sql')
SEED_PATH = Path('db/seed.sql')


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON;')
    return conn


def init_db():
    with get_conn() as conn:
        conn.executescript(SCHEMA_PATH.read_text())
        count = conn.execute('SELECT COUNT(*) AS c FROM animals').fetchone()['c']
        if count == 0:
            conn.executescript(SEED_PATH.read_text())
        conn.commit()
