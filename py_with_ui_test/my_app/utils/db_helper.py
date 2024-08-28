import sqlite3
from configparser import ConfigParser
import logging

def get_db_path():
    # Load database path from configuration file
    config = ConfigParser()
    config.read('config.ini')
    return config.get('database', 'db_path')

# Use a default path if config.ini is not available or not used
# def get_db_path():
#     return 'data.db'

def create_table():
    db_path = get_db_path()
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')
            conn.commit()
    except Exception as e:
        logging.error(f"Error creating table: {str(e)}", exc_info=True)

def fetch_data():
    db_path = get_db_path()
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM data')
        return cursor.fetchall()

def insert_data(name, value):
    db_path = get_db_path()
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO data (name, value) VALUES (?, ?)', (name, value))
        conn.commit()
