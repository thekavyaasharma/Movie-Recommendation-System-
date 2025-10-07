import streamlit as st
import pickle 
import pandas as pd
import requests # to hit the api 

def fetch_poster(movie_name):
    response = requests.get('https://www.omdbapi.com/?t={}&apikey=260fee98'.format(movie_name))
    data = response.json()
    return data['Poster']

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# fxn -> give movie name -> returns a list of 9 similar movies 
def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x: x[1])[1:10]

    # create a list to store movies
    recommended_movies = []
    recommend_movie_poster = []
    for i in movies_list:
        movie_name = movies['title'].iloc[i[0]]
        # fetch movie poster using api 
        recommend_movie_poster.append(fetch_poster(movie_name))

        # fetch movie names 
        recommended_movies.append(movies['title'].iloc[i[0]])
    
    return recommended_movies, recommend_movie_poster 

# Title 
st.markdown("""
    <div style="
        background-color: #D62828;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 35px;
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    ">
        🎬 Movie Recommendation System
    </div>
    <h4 style='text-align: center; color: #555;'>
        Content-Based Movie Recommender using TMDB Dataset
    </h4>
""", unsafe_allow_html=True)

# Collapsible Introduction Section
with st.expander("📘 Show Project Introduction"):
    st.markdown("""
    Welcome to the **Movie Recommendation System**, an intelligent web application that suggests movies similar to your favorites!  

    This Data Science project is a **Content-Based Recommendation System** built using the **TMDB (The Movie Database)** dataset.  
    It leverages natural language processing (NLP) techniques to analyze movie features such as **genres, keywords, cast, and overview**,  
    and then computes similarity scores to recommend the most relevant titles.

    The underlying model has been trained and optimized to provide up to **9 similar movie recommendations** for any selected title.
    """)

    # Key Highlights
    st.subheader("Key Highlights :")
    st.markdown("""
    - Built using **Python** and **Streamlit** for an interactive user interface  
    - Uses **Content-Based Filtering** to generate personalized movie suggestions  
    - Employs **vectorization and cosine similarity** to measure movie relevance  
    - Dataset sourced from **TMDB**, ensuring rich and reliable movie information  

    This project demonstrates how **Data Science and Machine Learning** can power real-world recommendation engines similar to those used by **Netflix** and **IMDb**.
    """)

#  another expander for About Dataset
with st.expander("📊 About the TMDB Dataset"):
    st.markdown("""
    The TMDB dataset contains detailed movie metadata including:
    - Title, Overview, and Tagline  
    - Cast and Crew information  
    - Genre and Keywords  
    
    These features are used to build text-based similarity scores that power this recommendation system.
    """)

selected_movie_name = st.selectbox(
    "Select Movie",
    movies['title'].values,
    index=None,
    placeholder="Enter name of the movie here ",
    
)

st.write("You selected:", selected_movie_name)

if st.button("Recommend"):
    names, poster =  recommend(selected_movie_name)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.text(names[0])
        st.image(poster[0], use_container_width = True )

    with col2:
        st.text(names[1])
        st.image(poster[1], use_container_width = True)

    with col3:
        st.text(names[2])
        st.image(poster[2], use_container_width = True)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.text(names[3])
        st.image(poster[3], use_container_width = True)

    with col5:
        st.text(names[4])
        st.image(poster[4], use_container_width = True)

    with col6:
        st.text(names[5])
        st.image(poster[5], use_container_width = True)

    col7, col8, col9 = st.columns(3)

    with col7:
        st.text(names[6])
        st.image(poster[6], use_container_width = True)

    with col8:
        st.text(names[7])
        st.image(poster[7], use_container_width = True)

    with col9:
        st.text(names[8])
        st.image(poster[8], use_container_width = True)
