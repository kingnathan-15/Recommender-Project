# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests
import sqlite3
from api import recommendation_identification
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./data/anime.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    if not query:
        return jsonify([])
    
    conn = get_db_connection()
    
    # Search only in anime name field
    cursor = conn.execute('''
        SELECT anime_id, name 
        FROM anime 
        WHERE name LIKE ? 
        ORDER BY 
            CASE 
                WHEN name LIKE ? THEN 1  -- Exact start match
                WHEN name LIKE ? THEN 2  -- Contains match
                ELSE 3
            END,
            name
        LIMIT 15
    ''', (f'%{query}%', f'{query}%', f'%{query}%'))
    
    results = []
    for row in cursor:
        results.append({
            'anime_id': row['anime_id'],
            'name': row['name']
        })
    
    conn.close()
    return jsonify(results)

@app.route('/api/anime/<anime_id>')
def get_anime_details(anime_id):
    try:
        # Make the request to MyAnimeList API from your server
        response = requests.get(
            f'https://api.myanimelist.net/v2/anime/{anime_id}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,rank,popularity,media_type,genres',
            headers={
                'X-MAL-CLIENT-ID': 'e863fdfe943adee262553933a60982f8'
            }
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/create_user_recommendations', methods=['POST'])
def recommendation_get():
    data = request.get_json()
    anime_id = int(data.get('anime_id'))
    print("Received anime_id:", anime_id)

    result = recommendation_identification(anime_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)