import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
  """Recommends similar movies based on user selection."""
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
  recommended_movies = []

  for i in movies_list:
    recommended_movies.append(movies.iloc[i[0]].title)

  return recommended_movies

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Set page title and layout
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Title and description (optional)
st.header('Movie Recommender')
st.image("MRS.jpg", use_column_width=True)
st.write("Find your next movie obsession!")

# Sidebar for movie selection with a clearer label
st.sidebar.header('Select a Movie')
selected_movie_name = st.sidebar.selectbox(
  'What movie would you like recommendations for?',  # More descriptive label
  movies['title'].values
)

if st.button('Recommend'):
  recommendations = recommend(selected_movie_name)

  movie_names = [movie[1:].title() for movie in recommendations]

  # Display recommended movies in a list format with a heading
  st.write("Recommended Movies:")
  for movie in movie_names:
    st.write(f"- {movie}")
