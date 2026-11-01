
import sqlite3
from pathlib import Path

from database.schema import CREATE_TABLES

DB_PATH = Path(__file__).resolve().parent / "trust_ai.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    try:
        connection.executescript(CREATE_TABLES)
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()
    print("TRUST-AI database created successfully!")
    print("Database location:", DB_PATH)
