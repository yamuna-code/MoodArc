# enrich_sentiment.py
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

DB_PATH = 'data/moodarc.db'

def process_lyric_sentiment():
    print("Initializing VADER Sentiment Intensity Analyzer...")
    analyzer = SentimentIntensityAnalyzer()
    
    # 1. Connect to the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 2. Fetch all tracks that have lyrics available
    cursor.execute("SELECT track_id, name, lyrics FROM tracks WHERE lyrics IS NOT NULL")
    tracks = cursor.fetchall()
    
    if not tracks:
        print("No tracks with lyrics found in the database. Run pipeline.py first!")
        conn.close()
        return
        
    print(f"Loaded {len(tracks)} tracks for sentiment analysis. Processing...")
    
    # 3. Loop through each track and calculate sentiment
    for track_id, track_name, lyrics in tracks:
        # VADER returns a dictionary with negative, neutral, positive, and compound scores.
        # The 'compound' score ranges from -1 (extremely negative) to +1 (extremely positive).
        scores = analyzer.polarity_scores(lyrics)
        valence_score = scores['compound']
        
        # 4. Update the database row with our engineered metric
        cursor.execute('''
            UPDATE tracks 
            SET lyric_sentiment = ? 
            WHERE track_id = ?
        ''', (valence_score, track_id))
        
        print(f"  ↳ Analyzed: {track_name} | Sentiment Valence: {valence_score:+.2f}")
        
    # Commit all changes and close the database connection
    conn.commit()
    conn.close()
    print("\nDatabase enriched successfully with Lyrical Sentiment metrics!")

if __name__ == "__main__":
    process_lyric_sentiment()