import sqlite3
from configparser import ConfigParser

def get_db_path():
    config = ConfigParser()
    config.read('config.ini')
    return config.get('database', 'db_path')

def create_table():
    db_path = get_db_path()
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')
        conn.commit()

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
