import streamlit as st
import pandas as pd

from src.hybrid_recommender import recommend_hybrid


st.set_page_config(
    page_title="BookNest",
    page_icon="📚"
)


# Load book data
books = pd.read_csv("Data/books_features.csv")

book_titles = books["title"].tolist()


# Title
st.title("📚 BookNest")

st.write("Discover your next great read.")


# Book selection
selected_book = st.selectbox(
    "Choose a book:",
    book_titles
)


# Recommendation button
if st.button("✨ Recommend Books"):

    recommendations = recommend_hybrid(selected_book)


    # Add information needed by the website
    recommendations = recommendations.merge(
        books[
            [
                "book_id",
                "image_url",
                "average_rating",
                "original_publication_year"
            ]
        ],
        on="book_id",
        how="left"
    )


    st.subheader("Recommended Books")


    # Display recommendations
    for _, book in recommendations.iterrows():

        col1, col2 = st.columns([1, 3])


        # Book cover
        with col1:

            if pd.notna(book["image_url"]):

                st.image(
                    book["image_url"],
                    width=130
                )


        # Book information
        with col2:

            st.markdown(
                f"### {book['title']}"
            )

            st.write(
                f"by {book['authors']}"
            )


            if pd.notna(book["average_rating"]):

                st.write(
                    f"⭐ {book['average_rating']:.2f}"
                )


            if pd.notna(book["original_publication_year"]):

                st.write(
                    f"Published: "
                    f"{int(book['original_publication_year'])}"
                )


        st.divider()