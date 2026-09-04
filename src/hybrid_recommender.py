import pandas as pd
import numpy as np

from src.content_recommender import (
    books_features,
    content_similarity,
    title_to_index
)

from src.collaborative_recommender import (
    book_ids,
    user_item_matrix,
    collaborative_model
)


# Final BookNest model configuration

FINAL_ALPHA = 0.3
FINAL_K = 10


def recommend_hybrid(title, alpha=FINAL_ALPHA, n=FINAL_K):

    # Check whether the book exists
    if title not in title_to_index:
        return pd.DataFrame()

    # Get the book's index
    content_idx = title_to_index[title]

    # Get the actual book_id
    book_id = books_features.iloc[content_idx]["book_id"]

    # -----------------------------
    # CONTENT-BASED SCORES
    # -----------------------------

    content_scores = content_similarity[content_idx]

    # -----------------------------
    # COLLABORATIVE SCORES
    # -----------------------------

    book_index = book_ids.cat.categories.get_loc(book_id)

    distances, indices = collaborative_model.kneighbors(
        user_item_matrix.T[book_index],
        n_neighbors=n + 1
    )

    collaborative_scores = np.zeros(len(books_features))

    similar_indices = indices[0][1:]
    similar_scores = 1 - distances[0][1:]

    similar_book_ids = book_ids.cat.categories[similar_indices]

    for similar_book_id, score in zip(
        similar_book_ids,
        similar_scores
    ):

        matching_rows = books_features.index[
            books_features["book_id"] == similar_book_id
        ]

        for row in matching_rows:
            collaborative_scores[row] = score

    # -----------------------------
    # HYBRID SCORE
    # -----------------------------

    hybrid_scores = (
        alpha * content_scores
        + (1 - alpha) * collaborative_scores
    )

    # Remove the original book
    hybrid_scores[content_idx] = -1

    # Get top recommendations
    top_indices = np.argsort(
        hybrid_scores
    )[::-1][:n]

    recommendations = books_features.iloc[
        top_indices
    ].copy()

    recommendations["content_score"] = (
        content_scores[top_indices]
    )

    recommendations["collaborative_score"] = (
        collaborative_scores[top_indices]
    )

    recommendations["hybrid_score"] = (
        hybrid_scores[top_indices]
    )

    return recommendations[
        [
            "book_id",
            "title",
            "authors",
            "content_score",
            "collaborative_score",
            "hybrid_score"
        ]
    ]