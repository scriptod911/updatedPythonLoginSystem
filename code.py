# Make a python login system using hashing and sql lite


import sqlite3
import hashlib
import sys
import os
import time


def create_table():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username text,
        password text,
        email text,
        date text
        )""")
    conn.commit()
    conn.close()


def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")
    date = time.asctime(time.localtime(time.time()))
    password = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", (username, password, email, date))
    conn.commit()
    conn.close()


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        print("Login successful")
    else:
        print("Login failed")


def main():
    create_table()
    while True:
        print("""
        1. Register
        2. Login
        3. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
    