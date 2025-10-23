import sqlite3
import csv

def create_anime_database(csv_filename, db_filename='data/anime.db'):
    # Connect to SQLite database
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    
    # Create anime table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS anime (
            anime_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    
    # Read CSV and insert data
    with open(csv_filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                cursor.execute(
                    'INSERT OR REPLACE INTO anime (anime_id, name) VALUES (?, ?)',
                    (int(row['anime_id']), row['name'])
                )
            except Exception as e:
                print(f"Error inserting row: {row} - {e}")
    
    # Commit changes and close connection
    conn.commit()
    
    # Verify data
    cursor.execute('SELECT COUNT(*) FROM anime')
    count = cursor.fetchone()[0]
    print(f"Successfully imported {count} records")
    
    conn.close()

# Usage
create_anime_database('data/anime.csv')