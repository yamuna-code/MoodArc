# engine.py
import sqlite3
import pandas as pd
import numpy as np

DB_PATH = 'data/moodarc.db'

def load_and_engineer_features():
    # 1. Connect and pull data into a Pandas DataFrame
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT track_id, name, lyrics, lyric_sentiment 
    FROM tracks 
    WHERE lyrics IS NOT NULL AND lyric_sentiment IS NOT NULL
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    if df.empty:
        print("No enriched data found in your database.")
        return df

    print(f"Loaded {len(df)} tracks into Pandas DataFrame for feature engineering...")

    # 2. FEATURE ENGINEERING: Calculate Text-Based Energy Proxy
    # Let's count total words in the lyrics
    df['word_count'] = df['lyrics'].apply(lambda x: len(str(x).split()))
    
    # Let's count unique words to see the vocabulary repetition rate
    df['unique_word_count'] = df['lyrics'].apply(lambda x: len(set(str(x).split())))
    df['repetition_index'] = 1 - (df['unique_word_count'] / (df['word_count'] + 1))

    # Min-Max Normalization to scale our Energy Proxy cleanly between 0.0 and 1.0
    min_rep = df['repetition_index'].min()
    max_rep = df['repetition_index'].max()
    
    # Handle edge case where max == min to prevent division by zero
    if max_rep == min_rep:
        df['energy_proxy'] = 0.5
    else:
        df['energy_proxy'] = (df['repetition_index'] - min_rep) / (max_rep - min_rep)

    # Rename lyric_sentiment to valence for clarity
    df = df.rename(columns={'lyric_sentiment': 'valence'})
    
    return df

def find_matching_tracks(target_valence, target_energy, df, top_n=3):
    """
    Calculates the Euclidean Distance between a user's desired emotional coordinate
    and the engineered vectors of the tracks in our database.
    """
    if df.empty:
        return []
        
    # User target vector
    target_vector = np.array([target_valence, target_energy])
    
    distances = []
    for idx, row in df.iterrows():
        # Track vector [Valence, Energy]
        track_vector = np.array([row['valence'], row['energy_proxy']])
        
        # Calculate standard Euclidean Distance: sqrt((x2-x1)^2 + (y2-y1)^2)
        distance = np.linalg.norm(target_vector - track_vector)
        distances.append(distance)
        
    df['match_distance'] = distances
    
    # Sort by closest distance (smallest numbers are the best matches)
    sorted_df = df.sort_values(by='match_distance').head(top_n)
    return sorted_df[['name', 'valence', 'energy_proxy', 'match_distance']].to_dict(orient='records')

if __name__ == "__main__":
    # Test our feature engineering engine
    data = load_and_engineer_features()
    
    if not data.empty:
        print("\nEngineered Feature Matrix Preview:")
        print(data[['name', 'valence', 'energy_proxy']].head())
        
        # Test a hypothetical user request from our Creative Sync Tool:
        # "Give me a song that is slightly sad/melancholic" -> Negative Valence (-0.5), Low Energy (0.2)
        print("\nTesting Matching Engine for a Melancholic Scene [-0.5, 0.2]:")
        matches = find_matching_tracks(target_valence=-0.5, target_energy=0.2, df=data)
        for rank, match in enumerate(matches, 1):
            print(f" Rank {rank}: {match['name']} | Distance: {match['match_distance']:.3f} (V: {match['valence']:.2f}, E: {match['energy_proxy']:.2f})")