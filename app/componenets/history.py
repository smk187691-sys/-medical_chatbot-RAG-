import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR,"chat_history.db")


def create_table():
    conn= sqlite3.connect(DB)
    c = conn.cursor()


    c.execute("""CREATE TABLE IF NOT EXISTS chats(id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL, answer TEXT NOT NULL,
        time TEXT)""")
    conn.commit()
    conn.close()

def save_chat(question,answer):
    conn= sqlite3.connect(DB)
    c=conn.cursor()

    c.execute("""
        INSERT INTO Chats(question, answer,time)
        VALUES (?,?,?)
        """,
        (question,answer,datetime.now().strftime("%Y-%m-%d %H-%M-%S")))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
        SELECT id, question,answer,time FROM chats
        ORDER BY ID ASC""")

    rows = c.fetchall()
    conn.close()
    return rows

def delet_chat(chat_id):
    conn= sqlite3.connect(DB)
    c= conn.cursor()

    c.execute(
        "DELETE FROM chats WHERE id = ?",
        (chat_id,)
    )

    conn.commit()
    conn.close()

def clear_history():
    conn= sqlite3.connect(DB)
    c= conn.cursor()

    c.execute(" DELETE FROM CHATS")
    conn.commit()
    conn.close()