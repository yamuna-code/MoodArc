# 🎧 MoodArc – AI-Powered Music Intelligence Platform

> **Mapping emotional trajectories in music using NLP and recommending songs for storytelling scenes.**

MoodArc is an AI-powered music analytics platform that transforms song lyrics into emotional intelligence. Instead of relying on Spotify's deprecated Audio Features API, MoodArc engineers its own emotional and pacing metrics using Natural Language Processing (NLP).

The project combines **data engineering**, **machine learning**, **text analytics**, and **interactive visualization** to help creators discover music that best matches the emotional tone of their content.

---

## 🚀 Live Demo

🔗 **Streamlit App:** [*https://moodarc.streamlit.app/*]
---

# 📖 Table of Contents

- [Problem Statement](#-problem-statement)
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Workflow](#-project-workflow)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [Project Structure](#-project-structure)
- [Author](#-author)
- [License](#-license)

---

# 🛑 Problem Statement

Most Spotify-based data science projects rely heavily on Spotify's precomputed **Audio Features API**.

However, in late **2024**, Spotify deprecated and restricted access to the `/audio-features` endpoint, making thousands of existing portfolio projects obsolete.

Instead of depending on proprietary black-box metrics, **MoodArc** generates its own emotional and structural song features directly from lyrics using Natural Language Processing.

This transforms a simple music visualization project into a scalable **Music Intelligence Platform** suitable for creators, analysts, and recommendation systems.

---

# 🎯 Project Overview

MoodArc analyzes lyrics to estimate:

- ❤️ Emotional Valence
- ⚡ Energy / Intensity
- 📝 Lexical Density
- 🔁 Repetition Index
- 📈 Structural Pacing

These engineered features are then used to:

- Visualize emotional shifts across artists
- Recommend songs for film scenes
- Match narrative emotion with music
- Build emotion-aware playlists

---

# ✨ Features

## 📊 1. Emotion Matrix

An interactive Plotly visualization that maps songs across an emotional landscape.

### X-Axis

**Valence Score**

Calculated using:

- VADER Sentiment Analyzer
- Lyric polarity
- Compound sentiment score

---

### Y-Axis

**Energy Proxy**

Engineered using textual characteristics such as:

- Word count
- Vocabulary richness
- Repetition ratio
- Lexical density
- Structural pacing

This provides a reasonable approximation of song intensity without requiring audio signal processing.

---

## 🎬 2. AI Scene Sync Tool

A recommendation engine designed for:

- Video Editors
- Filmmakers
- Content Creators
- Storytellers

Users simply describe a scene, for example:

> *"A heartbreaking goodbye in the rain."*

MoodArc then:

1. Performs sentiment analysis on the scene description.
2. Calculates the target emotional coordinates.
3. Compares them against every song stored in the database.
4. Uses Euclidean Distance to identify the closest emotional match.
5. Returns the most suitable songs.

---

## 📈 3. Interactive Dashboard

Built with **Streamlit** and **Plotly**, featuring:

- Interactive scatter plots
- Hover information
- Artist filtering
- Emotional analytics
- Dynamic recommendations

---

# 🏗️ Architecture

```
Spotify API
       │
       ▼
Track Metadata

LyricsGenius API
       │
       ▼
Song Lyrics

       │
       ▼
SQLite Database

       │
       ▼
NLP Processing
(VADER Sentiment)

       │
       ▼
Feature Engineering

       │
       ▼
Recommendation Engine

       │
       ▼
Streamlit Dashboard
```

---

# 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| Data Collection | Spotipy |
| Lyrics | LyricsGenius |
| Database | SQLite |
| NLP | NLTK, VADER |
| Data Analysis | Pandas |
| Numerical Computing | NumPy |
| Visualization | Plotly |
| Dashboard | Streamlit |

---

# ⚙️ Project Workflow

```
Spotify API
        ↓

Collect Track Metadata
        ↓

Scrape Lyrics
        ↓

Store in SQLite
        ↓

Run Sentiment Analysis
        ↓

Engineer Emotional Features
        ↓

Generate Emotion Matrix
        ↓

Recommend Songs
```

---

# 📦 Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/MoodArc.git

cd MoodArc
```

Create a virtual environment.

### Windows

```bash
python -m venv venv

.\venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a file named

```python
config.py
```

Add your API credentials.

```python
SPOTIFY_CLIENT_ID = "your_client_id"

SPOTIFY_CLIENT_SECRET = "your_client_secret"

GENIUS_ACCESS_TOKEN = "your_genius_access_token"
```

⚠️ Never commit this file.

Add it to `.gitignore`.

```
config.py
```

---

# ▶️ Usage

## Step 1 — Collect Data

```bash
python pipeline.py
```

Downloads Spotify metadata and lyrics.

---

## Step 2 — NLP Enrichment

```bash
python enrich_sentiment.py
```

Calculates:

- Sentiment
- Emotional Valence
- Energy Proxy
- Lexical Features

---

## Step 3 — Launch Dashboard

```bash
streamlit run app.py
```

Open the local Streamlit URL in your browser.

---

# 📂 Project Structure

```
MoodArc/

│

├── app.py

├── pipeline.py

├── enrich_sentiment.py

├── config.py

├── requirements.txt

├── database/

│   └── moodarc.db

├── assets/

│   ├── dashboard.png

│   ├── emotion_matrix.png

│   └── demo.gif

├── notebooks/

├── README.md

└── .gitignore
```

---

# 🔮 Future Improvements

## 🎵 Audio Signal Processing

Integrate **Librosa** to extract:

- BPM
- Tempo
- Spectral Centroid
- MFCC Features
- Zero Crossing Rate

using Spotify preview audio.

---

## 🤖 Transformer-Based NLP

Replace VADER with:

- DistilBERT
- RoBERTa
- Sentence Transformers

for more contextual understanding of lyrics.

---

## ☁️ Cloud Deployment

Move from SQLite to:

- PostgreSQL
- Supabase
- AWS RDS

for scalable production deployment.

---

## 🎼 Playlist Generation

Generate automatic playlists based on:

- Mood
- Story Arc
- Film Genre
- Emotional Journey

---

## 📱 Mobile Interface

Build a responsive frontend using:

- React
- Next.js
- Flutter

---

# 💡 Why This Project?

Unlike traditional Spotify analytics projects, MoodArc is resilient against API restrictions by engineering emotional features directly from lyrical content.

It demonstrates practical skills in:

- Data Engineering
- Natural Language Processing
- Recommendation Systems
- Data Visualization
- Interactive Dashboard Development
- Feature Engineering
- Python Backend Development

making it an excellent portfolio project for Data Science, Machine Learning, and AI roles.

---

# 👨‍💻 Author

**Yamuna**

Second-Year Data Science Student

- LinkedIn: https://linkedin.com/in/yamuna-sharma-6aa0a1321
- Email: yamunasharma2745@email.com

---
