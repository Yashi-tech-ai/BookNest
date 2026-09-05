import math

from src.content_recommender import recommend_content
from src.collaborative_recommender import recommend_collaborative
from src.hybrid_recommender import recommend_hybrid


TEST_TITLE = "The Hunger Games (The Hunger Games, #1)"
TEST_BOOK_ID = 1


def test_content_recommender():
    recommendations = recommend_content(TEST_TITLE)

    assert len(recommendations) == 10
    assert TEST_TITLE not in recommendations["title"].values


def test_collaborative_recommender():
    recommendations = recommend_collaborative(TEST_BOOK_ID)

    assert len(recommendations) == 10
    assert TEST_BOOK_ID not in recommendations["book_id"].values


def test_hybrid_recommender():
    recommendations = recommend_hybrid(TEST_TITLE)

    assert len(recommendations) == 10
    assert TEST_TITLE not in recommendations["title"].values


def test_hybrid_scores():
    recommendations = recommend_hybrid(TEST_TITLE)

    for _, row in recommendations.iterrows():
        expected_score = (
            0.3 * row["content_score"]
            + 0.7 * row["collaborative_score"]
        )

        assert math.isclose(
            row["hybrid_score"],
            expected_score,
            rel_tol=1e-9
        )