import sqlite3
import csv
import re

DATABASE = 'movies.db'

def clean_rating(val):
    """Convert rating string to float"""
    if not val or val.strip() == '':
        return None
    try:
        return float(str(val).strip())
    except:
        return None

def clean_number(val):
    """Convert number strings (with K, M) to integers"""
    if not val or val == 'NIL' or val.strip() == '':
        return 0
    
    val_str = str(val).strip().upper()
    
    # Remove any currency symbols and commas
    val_str = val_str.replace('$', '').replace(',', '')
    
    # Handle K (thousands)
    if 'K' in val_str:
        try:
            return int(float(val_str.replace('K', '')) * 1000)
        except:
            return 0
    
    # Handle M (millions)
    if 'M' in val_str:
        try:
            return int(float(val_str.replace('M', '')) * 1000000)
        except:
            return 0
    
    # Try parsing as regular number
    try:
        # Remove decimal for user reviews
        if '.' in val_str:
            return int(float(val_str))
        return int(val_str)
    except:
        return 0

def parse_watch_hours(val):
    """Extract hours from 'X hours Y minutes' format"""
    if not val or val.strip() == '':
        return None
    
    val_str = str(val).strip().lower()
    try:
        # Find hours
        hours_match = re.search(r'(\d+)\s*hours?', val_str)
        hours = int(hours_match.group(1)) if hours_match else 0
        
        # Find minutes
        minutes_match = re.search(r'(\d+)\s*minutes?', val_str)
        minutes = int(minutes_match.group(1)) if minutes_match else 0
        
        total_minutes = hours * 60 + minutes
        return total_minutes if total_minutes > 0 else None
    except:
        return None

def init_database():
    """Initialize database and load data from CSV"""
    
    # Create connection
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Drop existing table if it exists
    cursor.execute('DROP TABLE IF EXISTS movies')
    
    # Create table
    cursor.execute('''
        CREATE TABLE movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER,
            duration_minutes INTEGER,
            rating REAL,
            rated_by INTEGER,
            industry TEXT,
            genre TEXT,
            director TEXT,
            box_office INTEGER,
            user_reviews INTEGER,
            awards TEXT,
            description TEXT,
            streaming_platform TEXT,
            verdict TEXT
        )
    ''')
    
    # Read and insert CSV data
    movie_count = 0
    with open('movies.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            try:
                cursor.execute('''
                    INSERT INTO movies 
                    (name, year, duration_minutes, rating, rated_by, industry, genre, director, 
                     box_office, user_reviews, awards, description, streaming_platform, verdict)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['MOVIE NAME '].strip(),
                    int(row['Year of release']) if row['Year of release'].strip() else None,
                    parse_watch_hours(row['Watch  hour ']),
                    clean_rating(row['Ratings']),
                    clean_number(row['Ratedby']),
                    row['Film Industry'].strip() if row.get('Film Industry') else '',
                    row['Genre'].strip() if row.get('Genre') else '',
                    row['Director'].strip() if row.get('Director') else '',
                    clean_number(row['Box office collection']),
                    clean_number(row['User reviews']),
                    row['Awards'].strip() if row.get('Awards') else '',
                    row['Description'].strip() if row.get('Description') else '',
                    row['Streaming platform'].strip() if row.get('Streaming platform') else '',
                    row['Verdict'].strip() if row.get('Verdict') else ''
                ))
                movie_count += 1
            except Exception as e:
                print(f"Error inserting row: {e}")
                continue
    
    # Create indexes for better query performance
    cursor.execute('CREATE INDEX idx_rating ON movies(rating DESC)')
    cursor.execute('CREATE INDEX idx_year ON movies(year)')
    cursor.execute('CREATE INDEX idx_industry ON movies(industry)')
    cursor.execute('CREATE INDEX idx_name ON movies(name)')
    
    conn.commit()
    conn.close()
    
    print(f"Database initialized successfully!")
    print(f"Total movies inserted: {movie_count}")

if __name__ == '__main__':
    init_database()
