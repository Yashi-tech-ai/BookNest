import streamlit as st
import pandas as pd

from src.hybrid_recommender import recommend_hybrid


st.set_page_config(
    page_title="BookNest",
    page_icon="📚"
)

st.title("📚 BookNest")
st.write("Discover your next great read.")

books = pd.read_csv("Data/books_features.csv")

book_titles = books["title"].tolist()

selected_book = st.selectbox(
    "Choose a book:",
    book_titles
)

if st.button("✨ Recommend Books"):
    recommendations = recommend_hybrid(selected_book)

    st.subheader("Recommended Books")

    for _, book in recommendations.iterrows():
        st.write(f"**{book['title']}**")
        st.write(f"by {book['authors']}")
        st.write("---")