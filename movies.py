# IMDB_Movie_Analysis

# Import the Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

# Importing the csv file

df = pd.read_csv('IMDB_Movies.csv')

# Setting up page configuration

st.set_page_config(page_title= "IMDB Movie Analysis With PowerBI",
                   layout= "wide",
                   initial_sidebar_state= "expanded"                   
                  )

# Creating option menu in the side bar

with st.sidebar:

    selected = option_menu("Menu", ["Home","Movie Analysis"], 
                           icons=["house","list-task"],
                           menu_icon= "menu-button-wide",
                           default_index=0,
                           styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "green"},
                                   "nav-link-selected": {"background-color": "green"}}
                          )
    
if selected == 'Home':

    st.title(":green[*IMDB Movie Analysis With PowerBI*]")
    
    col1, col2 = st.columns(2)

    with col1:
        col1.markdown("# ")
        col1.markdown("# ")
        col1.markdown("## :violet[*Overview*] : Creating a dashboard with PowerBI/Tableau to analyze movie data")
        col1.markdown("# ")
        col1.markdown("## :violet[*Domain*] : Movie")
        col1.markdown("# ")
        col1.markdown("## :violet[*Technologies used*] : Python, Pandas, Numpy, Matplotlib, Seaborn, Streamlit, Tableau.")

    with col2:
        col2.markdown("# ")
        col2.markdown("# ")
        col2.image("/Users/arul/Downloads/IMDb_Header_Page.jpg")
        col2.markdown("# ")
        col2.image("/Users/arul/Downloads/movies2.jpg")
        col2.markdown("# ")
        col2.image("/Users/arul/Downloads/home22.jpg")

if selected == 'Movie Analysis':

    st.title(":red[*Movie Analysis FAQ*]")


    questions = st.selectbox("Select Your Questions",("01. Why do movies with higher budgets tend to have higher ratings?",
                                                        "02. Why does better production quality lead to higher ratings?",
                                                        "03. Why does an enhanced viewer experience lead to higher ratings?",
                                                        "04. Why are viewers more likely to rate a movie highly if they enjoyed watching it?",
                                                        "05. Why do positive reviews matter?"
                                                        ))
    st.markdown("# ")
    st.markdown("## :violet[*ANSWER:*]")
    st.markdown("# ")
    if questions == "01. Why do movies with higher budgets tend to have higher ratings?":
        st.markdown("Higher budgets allow for better production quality, including advanced special effects, top-tier actors, and impressive set designs. This can contribute to a more visually appealing and immersive movie-watching experience.")
        col1, col2 = st.columns(2)
        col1.markdown("# ")
        col1.image("/Users/arul/Downloads/budget1.jpg")
        col2.markdown("# ")
        col2.markdown("# ")
        col2.image("/Users/arul/Downloads/productivity.jpeg")


    if questions == "02. Why does better production quality lead to higher ratings?":
        st.markdown("Better production quality enhances the overall viewer experience by providing clearer visuals, realistic effects, and improved sound design. A movie's ability to captivate the audience with high-quality production elements often translates to higher ratings")
        col1, col2 = st.columns(2)
        col1.markdown("# ")
        col1.markdown("# ")
        col1.image("/Users/arul/Downloads/product1.jpg")
        col2.markdown("# ")
        col2.image("/Users/arul/Downloads/Rating.jpg")

    if questions == "03. Why does an enhanced viewer experience lead to higher ratings?":
        st.markdown("An enhanced viewer experience ensures that the audience remains engaged and entertained throughout the movie. When viewers enjoy the film, they are more likely to have a positive emotional response, leading to higher ratings.")
        col1, col2 = st.columns(2)
        col1.markdown("# ")
        col1.image("/Users/arul/Downloads/emotion.jpg")
        col2.markdown("# ")
        col2.image("/Users/arul/Downloads/Star-Rating-reviews.jpg")

    if questions == "04. Why are viewers more likely to rate a movie highly if they enjoyed watching it?":
        st.markdown("Positive emotions and enjoyment create a favorable impression of the movie. Viewers tend to associate positive experiences with higher ratings, as they are more inclined to express satisfaction through positive reviews.")
        col1, col2 = st.columns(2)
        col1.markdown("# ")
        col1.image("/Users/arul/Downloads/emotions1.jpg")
        col2.markdown("# ")
        col2.image("/Users/arul/Downloads/p_ratings.jpg")

    if questions == "05. Why do positive reviews matter?":
        st.markdown("Positive reviews serve as endorsements from viewers who have already enjoyed the movie. These reviews can influence other potential viewers, building anticipation and interest in the film. As positive word-of-mouth spreads, it increases the movie's popularity, contributing to its overall success.")
        col1, col2 = st.columns(2)
        col1.markdown("# ")
        col1.markdown("# ")
        col1.image("/Users/arul/Downloads/customer-loyalty.jpg")
        col2.markdown("# ")
        col2.image("/Users/arul/Downloads/Success-1.jpg")

    st.sidebar.markdown("## [TABLEAU DASHBORD](https://public.tableau.com/app/profile/ramya.krishnan.a8410/viz/IMDB_Movie_Analysis_2/Dashboard12#2)")

    

   
    