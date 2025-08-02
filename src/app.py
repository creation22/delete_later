from flask import Flask
from routes import setup_routes
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_change_in_production'

# Initialize database
def init_db():
    conn = sqlite3.connect('incidents.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Create database on startup
init_db()

setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)