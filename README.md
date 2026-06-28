🎧 MoodArc: Music Intelligence Platform

An AI-powered data product mapping emotional trajectories and syncing music to narrative scenes.

🚀 Live Demo: Click here to view the live Streamlit App
(Replace the link above once you deploy!)

🛑 The Problem & The Pivot

Most "Spotify Data Science" projects rely on surface-level feature engineering, pulling pre-calculated API metrics to predict a static number. Furthermore, in late 2024, Spotify deprecated and locked their /audio-features endpoint, breaking thousands of portfolio projects worldwide.

MoodArc flips this problem into an engineering feature. Instead of relying on black-box corporate metrics, this project bypasses the restriction by engineering custom emotional and pacing proxies purely through Text Mining and Natural Language Processing (NLP) of song lyrics.

It elevates a standard music-analysis script into a functional B2B Creator Tool.

✨ Core Features

1. 📊 The Emotion Matrix (Macro Analytics)

An interactive, multi-axis scatter plot visualizing the emotional shift across multiple artists' discographies.

X-Axis (Valence): Engineered using the VADER Sentiment Analyzer on raw scraped lyric text.

Y-Axis (Energy Proxy): Engineered by calculating lexical density, vocabulary repetition ratios, and structural text pacing.

2. 🎬 AI Scene Sync Tool (Micro Application)

A Natural Language search engine built for video editors and filmmakers.

Users describe their video scene (e.g., "A heartbreaking goodbye in the rain").

The backend NLP engine calculates the target emotional valence in real-time.

A mathematical recommendation algorithm uses Euclidean Distance to map the scene's coordinates against the SQL database, returning the best-fit tracks.

( 📸 Pro-Tip: Add a GIF recording of your Streamlit app in action right here!)

🛠️ Technical Architecture

Component

Technology

Description

Data Ingestion

Spotipy, LyricsGenius

Extracts track metadata and lyrics, handling API rate limits and pagination.

Storage

SQLite

Stores clean, relational data directly on disk for high-speed local reads.

NLP Enrichment

VADER Sentiment

Processes thousands of lyric lines to extract normalized polarity scores (-1.0 to +1.0).

Engine

Pandas, NumPy

Calculates structural text features (word count, repetition index) and vector distances.

Frontend UI

Streamlit, Plotly

Renders a responsive, interactive web dashboard.

💻 Quick Start Guide

1. Clone & Set Up

git clone [https://github.com/yourusername/MoodArc.git](https://github.com/yourusername/MoodArc.git)
cd MoodArc
python -m venv venv

# Activate Environment (Windows)
.\venv\Scripts\Activate.ps1
# Activate Environment (Mac/Linux)
source venv/bin/activate

pip install -r requirements.txt


2. Configure Credentials

Create a config.py file in the root directory:

SPOTIFY_CLIENT_ID = "your_spotify_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_secret"
GENIUS_ACCESS_TOKEN = "your_genius_token"


(Ensure config.py is added to your .gitignore!)

3. Build & Run

# Scrape the data and build the database
python pipeline.py

# Run NLP enrichment on the raw text
python enrich_sentiment.py

# Launch the live dashboard
streamlit run app.py


🔮 Future Roadmap

[ ] Audio-Signal Processing: Integrate librosa to extract raw waveform features (BPM, spectral centroid) from 30-second preview MP3s.

[ ] LLM Integration: Replace VADER with a lightweight local transformer (e.g., DistilBERT) for deeper contextual embedding of sarcastic lyrics.

[ ] Cloud Database: Migrate from local SQLite to PostgreSQL (Supabase/AWS) for scalable production deployment.

Created by Yamuna
