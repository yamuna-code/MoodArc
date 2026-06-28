🎧 MoodArc: Music Intelligence & Sync Platform

MoodArc is an end-to-end data product and AI-powered platform designed to map the emotional trajectory of artist discographies and help video creators find the perfect mathematical track match for their narrative scenes.

The Problem & The Pivot

Most "Spotify Data Science" projects rely on surface-level feature engineering, simply pulling pre-calculated API metrics to predict a static number. Furthermore, in late 2024, Spotify deprecated and locked their /audio-features endpoint to independent developers.

MoodArc flips this problem into an engineering feature. Instead of relying on black-box corporate metrics, this project bypasses the restriction by engineering custom emotional and pacing proxies purely through Text Mining and Natural Language Processing (NLP) of song lyrics.

It upgrades the standard music-analysis project from a simple exploratory script into a B2B Creator Tool.

Core Features

1. 📊 The Emotion Matrix (Macro Analytics)

An interactive, multi-axis scatter plot that visualizes the emotional shift across multiple artists' discographies.

X-Axis (Valence): Engineered using the VADER Sentiment Analyzer on raw lyric text.

Y-Axis (Energy Proxy): Engineered by calculating lexical density, vocabulary repetition ratios, and structural text pacing.

2. 🎬 Creative Content Syncing Tool (Micro Application)

A Natural Language search engine for video editors and filmmakers.

Users type a description of their video scene (e.g., "A heartbreaking goodbye in the rain").

The backend NLP engine calculates the target valence of the text in real-time.

A recommendation algorithm uses Euclidean Distance to map the scene's emotional coordinates against the database, returning the mathematical best-fit tracks.

🛠️ Technical Architecture

ETL Pipeline (pipeline.py): Integrates the Spotipy (Spotify) and LyricsGenius APIs. Handles rate-limiting, pagination, and data cleaning, storing raw text and metadata into a local SQLite relational database.

NLP Enrichment (enrich_sentiment.py): Connects to the database and processes thousands of lines of lyrics through VADER to extract normalized polarity scores (-1.0 to +1.0).

Recommendation Engine (engine.py): Uses Pandas and NumPy to calculate structural text features (word count, repetition index) and scales them via Min-Max normalization to create an Energy Proxy. Computes vector distances for matchmaking.

Interactive UI (app.py): A responsive web dashboard built with Streamlit and Plotly.

💻 How to Run Locally

1. Clone the repository and set up environment

git clone https://github.com/yourusername/MoodArc.git
cd MoodArc
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt


2. Configure API Keys

Create a file named config.py in the root directory and add your developer credentials:

SPOTIFY_CLIENT_ID = "your_spotify_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_secret"
GENIUS_ACCESS_TOKEN = "your_genius_token"


3. Build the Database

Run the pipeline scripts in order to scrape the data and engineer the NLP features:

# 1. Scrapes Spotify and Genius, builds SQLite DB (~5-10 mins for large batches)
python pipeline.py

# 2. Runs VADER NLP on the scraped lyrics to generate sentiment scores
python enrich_sentiment.py


4. Launch the App

streamlit run app.py


🔮 Future Roadmap

Audio-Signal Processing: Integrate librosa to extract raw waveform features (BPM, spectral centroid) from 30-second preview MP3s to supplement the text-based Energy Proxy.

LLM Integration: Replace VADER with a lightweight local transformer (e.g., DistilBERT) for deeper contextual embedding of sarcastic or highly metaphorical lyrics.

Cloud Database: Migrate from local SQLite to PostgreSQL (Supabase/AWS) for live production deployment.

Created by Yamuna 