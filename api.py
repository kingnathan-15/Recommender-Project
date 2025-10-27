from flask_cors import CORS
import joblib
import pandas as pd
import warnings
import numpy as np
from flask import Flask, request, jsonify
from scipy.sparse import coo_matrix, vstack
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app, supports_credentials=True)

recommender_model = joblib.load('model/KNN_Recommender.pkl')
anime_map=joblib.load('model/anime_map.pkl')
user_map=joblib.load('model/user_map.pkl')
reverse_anime_map=joblib.load('model/reverse_anime_map.pkl')
rating_df = pd.read_csv('data/rating.csv')
anime_df = pd.read_csv('data/anime.csv')

def create_interaction_matrix(df):
    

    chunks = np.array_split(rating_df, 20)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i}: {chunk.shape}")

    sparse_chunks = []
    for chunk in chunks:
        rows = chunk['user_id'].map(user_map)
        cols = chunk['anime_id'].map(anime_map)
        vals = chunk['rating'].astype(float)

        shape = (len(user_map), len(anime_map))
        sparse_chunk = coo_matrix((vals, (rows, cols)), shape=shape)
        sparse_chunks.append(sparse_chunk)

    interaction_matrix = vstack(sparse_chunks).tocsr()
    return interaction_matrix

interaction_matrix = create_interaction_matrix(rating_df)

def recommendation_identification(anime_id):
    target_idx = anime_map[anime_id]
    distances, indices = recommender_model.kneighbors(
        interaction_matrix.T[target_idx].reshape(1, -1),
        n_neighbors=5
    )

    similar_anime_ids = [int(reverse_anime_map[int(i)]) for i in indices.flatten()]
    
    result = {
        "similar_anime_ids": similar_anime_ids
    }

    for anime_id in similar_anime_ids:
        print(anime_df[anime_df['anime_id'] == anime_id]['name'].values[0])

    return result





if __name__ == '__main__':
    app.run(debug=True)