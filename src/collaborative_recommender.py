from pathlib import Path

import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

DATA_DIR = Path(__file__).resolve().parents[1] / "Data"

ratings = pd.read_csv(DATA_DIR / "ratings.csv")
books_features = pd.read_csv(DATA_DIR / "books_features.csv")


# Convert IDs to categorical values
user_ids = ratings["user_id"].astype("category")
book_ids = ratings["book_id"].astype("category")


# Create sparse user-item matrix
user_item_matrix = csr_matrix(
    (
        ratings["rating"].values,
        (user_ids.cat.codes, book_ids.cat.codes)
    )
)


# Collaborative filtering model
collaborative_model = NearestNeighbors(
    n_neighbors=11,
    metric="cosine",
    algorithm="brute",
    n_jobs=-1
)

collaborative_model.fit(user_item_matrix.T)


def recommend_collaborative(book_id, n=10):

    # Find the position of the book
    book_index = book_ids.cat.categories.get_loc(book_id)

    # Find similar books
    distances, indices = collaborative_model.kneighbors(
        user_item_matrix.T[book_index],
        n_neighbors=n + 1
    )

    similarities = 1 - distances[0]

    # Remove the original book
    similar_indices = indices[0][1:]
    similar_scores = similarities[1:]

    # Convert matrix indices back to book IDs
    similar_book_ids = book_ids.cat.categories[similar_indices]

    recommendations = books_features[
        books_features["book_id"].isin(similar_book_ids)
    ].copy()

    # Preserve recommendation order
    score_map = dict(
        zip(similar_book_ids, similar_scores)
    )

    recommendations["similarity"] = recommendations[
        "book_id"
    ].map(score_map)

    recommendations = recommendations.sort_values(
        "similarity",
        ascending=False
    )

    return recommendations[
        ["book_id", "title", "authors", "similarity"]
    ].head(n)