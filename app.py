from flask import Flask, render_template, jsonify
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)
DATABASE = 'movies.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def dict_from_row(row):
    """Convert sqlite3.Row to dictionary"""
    return dict(row) if row else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/movies')
def get_movies():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies ORDER BY rating DESC').fetchall()
    conn.close()
    return jsonify([dict(movie) for movie in movies])

@app.route('/api/stats')
def get_stats():
    conn = get_db_connection()
    
    # Get various statistics
    cursor = conn.cursor()
    
    # Overall stats
    total_movies = cursor.execute('SELECT COUNT(*) FROM movies').fetchone()[0]
    avg_rating = cursor.execute('SELECT AVG(rating) FROM movies').fetchone()[0]
    avg_reviews = cursor.execute('SELECT AVG(user_reviews) FROM movies').fetchone()[0]
    
    # Rating distribution
    rating_dist = cursor.execute('''
        SELECT 
            CASE 
                WHEN rating >= 9 THEN '9.0-10'
                WHEN rating >= 8.5 THEN '8.5-8.9'
                WHEN rating >= 8 THEN '8.0-8.4'
                WHEN rating >= 7 THEN '7.0-7.9'
                ELSE '<7'
            END as range,
            COUNT(*) as count
        FROM movies
        GROUP BY range
        ORDER BY range DESC
    ''').fetchall()
    
    # Top genres
    top_genres = cursor.execute('''
        SELECT genre, COUNT(*) as count, AVG(rating) as avg_rating
        FROM movies
        GROUP BY genre
        ORDER BY count DESC
        LIMIT 10
    ''').fetchall()
    
    # Top industries
    top_industries = cursor.execute('''
        SELECT industry, COUNT(*) as count, AVG(rating) as avg_rating
        FROM movies
        GROUP BY industry
        ORDER BY count DESC
    ''').fetchall()
    
    # Highest rated movies
    top_movies = cursor.execute('''
        SELECT name, rating, year, industry
        FROM movies
        ORDER BY rating DESC
        LIMIT 5
    ''').fetchall()
    
    conn.close()
    
    return jsonify({
        'total_movies': total_movies,
        'avg_rating': round(avg_rating, 2) if avg_rating else 0,
        'avg_reviews': round(avg_reviews, 0) if avg_reviews else 0,
        'rating_distribution': [{'range': r[0], 'count': r[1]} for r in rating_dist],
        'top_genres': [{'genre': g[0], 'count': g[1], 'avg_rating': round(g[2], 2)} for g in top_genres],
        'top_industries': [{'industry': i[0], 'count': i[1], 'avg_rating': round(i[2], 2)} for i in top_industries],
        'top_movies': [{'name': m[0], 'rating': m[1], 'year': m[2], 'industry': m[3]} for m in top_movies]
    })

@app.route('/api/search')
def search():
    from flask import request
    query = request.args.get('q', '').lower()
    
    if not query or len(query) < 2:
        return jsonify([])
    
    conn = get_db_connection()
    results = conn.execute('''
        SELECT * FROM movies 
        WHERE LOWER(name) LIKE ? 
        ORDER BY rating DESC
        LIMIT 20
    ''', (f'%{query}%',)).fetchall()
    conn.close()
    
    return jsonify([dict(movie) for movie in results])

@app.route('/api/filter')
def filter_movies():
    from flask import request
    
    min_rating = request.args.get('min_rating', 0, type=float)
    year = request.args.get('year', None, type=int)
    industry = request.args.get('industry', None)
    genre = request.args.get('genre', None)
    
    conn = get_db_connection()
    
    query = 'SELECT * FROM movies WHERE rating >= ?'
    params = [min_rating]
    
    if year:
        query += ' AND year = ?'
        params.append(year)
    if industry:
        query += ' AND industry = ?'
        params.append(industry)
    if genre:
        query += ' AND LOWER(genre) LIKE ?'
        params.append(f'%{genre.lower()}%')
    
    query += ' ORDER BY rating DESC'
    
    results = conn.execute(query, params).fetchall()
    conn.close()
    
    return jsonify([dict(movie) for movie in results])

@app.route('/api/genres')
def get_genres():
    conn = get_db_connection()
    genres = conn.execute('''
        SELECT DISTINCT genre FROM movies
        ORDER BY genre
    ''').fetchall()
    conn.close()
    return jsonify([g[0] for g in genres if g[0]])

@app.route('/api/industries')
def get_industries():
    conn = get_db_connection()
    industries = conn.execute('''
        SELECT DISTINCT industry FROM movies
        ORDER BY industry
    ''').fetchall()
    conn.close()
    return jsonify([i[0] for i in industries if i[0]])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
