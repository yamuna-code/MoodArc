import streamlit as st
import pandas as pd
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import engine 

# ==========================================
# 1. PAGE CONFIGURATION & INITIALIZATION
# ==========================================
st.set_page_config(page_title="MoodArc: Music Intelligence", page_icon="🎧", layout="wide")

@st.cache_data
def load_data():
    return engine.load_and_engineer_features()

@st.cache_resource
def load_analyzer():
    return SentimentIntensityAnalyzer()

df = load_data()
analyzer = load_analyzer()

# ==========================================
# 2. UI HEADER
# ==========================================
st.title("🎧 MoodArc: Music Intelligence Platform")
st.markdown("An AI-powered platform for exploring artist discographies and syncing music to narrative emotional arcs.")

if df.empty:
    st.error("No data found! Please run your pipeline.py and enrich_sentiment.py scripts first.")
    st.stop()

# Create two clean tabs
tab1, tab2 = st.tabs(["📊 The Emotion Matrix", "🎬 Creative Content Syncing Tool"])

# ==========================================
# 3. TAB 1: THE MACRO ANALYTICS DASHBOARD
# ==========================================
with tab1:
    st.header("Discography Emotion Matrix")
    st.markdown("Explore how tracks map across emotional Valence (Negative to Positive) and Lyrical Energy (Low to High).")
    
    # Beautiful interactive plot
    fig = px.scatter(
        df, 
        x="valence", 
        y="energy_proxy", 
        hover_name="name",
        color="valence", 
        color_continuous_scale="RdBu", 
        labels={"valence": "Negative ⬅️ Valence (Mood) ➡️ Positive", "energy_proxy": "Low ⬇️ Energy (Pacing) ⬆️ High"}
    )
    
    # Add quadrants
    fig.add_hline(y=0.5, line_width=1, line_dash="dash", line_color="gray", opacity=0.5)
    fig.add_vline(x=0.0, line_width=1, line_dash="dash", line_color="gray", opacity=0.5)
    
    # Clean UI layout
    fig.update_layout(height=600, xaxis_range=[-1.1, 1.1], yaxis_range=[-0.1, 1.1], margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# 4. TAB 2: THE MICRO SYNC TOOL (UPGRADED)
# ==========================================
with tab2:
    st.header("🎬 Natural Language Scene Matcher")
    st.markdown("Describe the emotion of your video scene, and our NLP engine will find the mathematical best-fit tracks.")
    
    col1, col2 = st.columns([1, 1.2]) # Make the results column slightly wider
    
    with col1:
        st.subheader("1. Describe Your Scene")
        scene_description = st.text_area(
            "What is happening emotionally?", 
            placeholder="e.g., A triumphant victory after a long, grueling battle...",
            height=100
        )
        
        st.subheader("2. Set the Pacing")
        target_energy = st.slider("How fast-paced is the edit?", min_value=0.0, max_value=1.0, value=0.5, step=0.1,
                                  help="0.0 = Slow, ambient, lingering shots. 1.0 = Fast cuts, high action.")
        
        match_button = st.button("🔮 Analyze & Find Tracks", use_container_width=True)

    with col2:
        st.subheader("Recommendations")
        
        if match_button:
            if not scene_description.strip():
                st.warning("Please describe your scene first!")
            else:
                # 1. NLP MAGIC: Calculate Valence from user's text
                sentiment_scores = analyzer.polarity_scores(scene_description)
                calculated_valence = sentiment_scores['compound']
                
                st.info(f"🧠 **AI Analysis:** Detected a target mood score of **{calculated_valence:.2f}**")
                
                # 2. Run the Engine
                matches = engine.find_matching_tracks(calculated_valence, target_energy, df, top_n=4)
                
                # 3. Display Results beautifully
                for i, match in enumerate(matches):
                    with st.expander(f"🎵 Rank {i+1}: **{match['name']}**", expanded=(i==0)):
                        m_col1, m_col2, m_col3 = st.columns(3)
                        m_col1.metric("Match Score", f"{1.0 - match['match_distance']:.2f}", help="Closer to 1.0 is better!")
                        m_col2.metric("Track Mood", f"{match['valence']:.2f}")
                        m_col3.metric("Track Energy", f"{match['energy_proxy']:.2f}")