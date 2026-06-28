import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import config
import sqlite3
import os
import time

# ==========================================
# 1. INITIALIZATION & SETUP
# ==========================================
auth_manager = SpotifyClientCredentials(
    client_id=config.SPOTIFY_CLIENT_ID, 
    client_secret=config.SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)
genius = lyricsgenius.Genius(config.GENIUS_ACCESS_TOKEN)
genius.verbose = False
genius.remove_section_headers = True

DB_PATH = 'data/moodarc.db'

def get_db_connection():
    return sqlite3.connect(DB_PATH)

# ==========================================
# 2. DATABASE OPERATIONS (INSERTIONS)
# ==========================================
def save_artist(artist_id, name, genres):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO artists (artist_id, name, genres) VALUES (?, ?, ?)', (artist_id, name, ', '.join(genres)))
    conn.commit()
    conn.close()

def save_album(album_id, artist_id, name, release_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO albums (album_id, artist_id, name, release_date) VALUES (?, ?, ?, ?)', (album_id, artist_id, name, release_date))
    conn.commit()
    conn.close()

def save_track_meta(track_id, album_id, name, lyrics):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO tracks (track_id, album_id, name, lyrics) 
        VALUES (?, ?, ?, ?)
    ''', (track_id, album_id, name, lyrics))
    conn.commit()
    conn.close()

# ==========================================
# 3. CORE PIPELINE LOGIC
# ==========================================
def scrape_lyrics_pipeline(artist_name, max_albums=2):
    print(f"Launching Music Text Mining Pipeline for: {artist_name}")
    
    search_results = sp.search(q=f"artist:{artist_name}", type='artist', limit=1)
    if not search_results['artists']['items']:
        print("Artist not found.")
        return
        
    artist_meta = search_results['artists']['items'][0]
    artist_id = artist_meta['id']
    official_name = artist_meta['name']
    
    save_artist(artist_id, official_name, artist_meta.get('genres', []))
    
    albums_results = sp.artist_albums(artist_id, album_type='album', limit=max_albums)
    
    for album in albums_results['items']:
        album_id = album['id']
        save_album(album_id, artist_id, album['name'], album.get('release_date', 'Unknown'))
        print(f"\nProcessing Album: {album['name']}")
        
        tracks_results = sp.album_tracks(album_id)
        for track in tracks_results['items']:
            track_id = track['id']
            track_name = track['name']
            
            print(f"  ↳ Scraping lyrics for: {track_name}...")
            lyrics = None
            try:
                genius_song = genius.search_song(track_name, official_name)
                if genius_song:
                    lyrics = genius_song.lyrics
            except Exception as e:
                print(f"     Genius error: {e}")
            
            # Save metadata and raw lyrics string to database
            save_track_meta(track_id, album_id, track_name, lyrics)
            time.sleep(0.5)
            
    print(f"\nDatabase successfully populated with lyrics for {official_name}!")

# ==========================================
# 4. BATCH EXECUTION RUNNER
# ==========================================
if __name__ == "__main__":
    # A curated list of diverse artists to give our engine a wide emotional range.
    artists_to_scrape = [
        "Taylor Swift",       # High emotional variance
        "Kendrick Lamar",     # High lyrical density / Energy
        "Adele",              # Low energy, high emotion ballads
        "Daft Punk",          # High energy, repetitive lyrics
        "Billie Eilish",      # Low energy, darker valence
        "Coldplay",           # Melancholic to triumphant rock
        "Drake",              # Hip-hop/R&B mix
        "Hozier",             # Poetic, slower indie
        "Dua Lipa",           # Upbeat, high danceability pop
        "Justin Bieber",      # Pop, R&B, varied energy
        "sombr",              # Indie, moody, emotional
        "Lana Del Rey",       # Cinematic, melancholic, low energy
        "BTS"                 # K-pop, high energy, dynamic
    ]

    print(f"Starting Batch Pipeline for {len(artists_to_scrape)} artists...\n")

    for artist in artists_to_scrape:
        try:
            # We limit to 3 albums per artist to keep the scrape time manageable for now.
            scrape_lyrics_pipeline(artist, max_albums=3)
            
            # The "Politeness" Timer: Wait 5 seconds between artists 
            print(f"Resting for 5 seconds before the next artist...")
            time.sleep(5) 
            
        except Exception as e:
            # If one artist totally fails, print the error but KEEP GOING to the next one
            print(f"CRITICAL ERROR processing {artist}: {e}")
            continue

    print("\nMASSIVE BATCH SCRAPE COMPLETE!")