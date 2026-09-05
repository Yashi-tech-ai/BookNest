from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_DIR = Path(__file__).resolve().parents[1] / "Data"

books_features = pd.read_csv(DATA_DIR / "books_features.csv")


# TF-IDF
tfidf = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

tfidf_matrix = tfidf.fit_transform(
    books_features["tag_name"]
)


# Content similarity
content_similarity = cosine_similarity(tfidf_matrix)


# Map book titles to dataframe indices
title_to_index = pd.Series(
    books_features.index,
    index=books_features["title"]
).to_dict()


def recommend_content(title, n=10):

    if title not in title_to_index:
        return pd.DataFrame()

    idx = title_to_index[title]

    scores = list(
        enumerate(content_similarity[idx])
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    scores = [
        (book_idx, score)
        for book_idx, score in scores
        if book_idx != idx
    ][:n]

    recommendations = books_features.iloc[
        [x[0] for x in scores]
    ].copy()

    recommendations["similarity"] = [
        x[1] for x in scores
    ]

    return recommendations[
        ["book_id", "title", "authors", "similarity"]
    ]