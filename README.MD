#  BookNest

A personalized book recommendation system built using hybrid
recommendation techniques and presented through a Streamlit web
application.

---

## Project Overview

BookNest is a book recommendation system built using the
Goodbooks-10k dataset.

The project explores multiple recommendation approaches and combines
content-based filtering with collaborative filtering to generate
hybrid book recommendations.

The final system is available as an interactive Streamlit web
application where users can select a book and receive ten recommended
books.

---

## Recommendation Approach

BookNest uses two recommendation techniques:

### 1. Content-Based Filtering

Content-based filtering recommends books based on their similarity
to the selected book using book metadata and tags.

TF-IDF vectorization and cosine similarity are used to calculate
content similarity.

### 2. Collaborative Filtering

Collaborative filtering identifies books with similar rating
patterns using the ratings dataset.

A k-nearest-neighbors approach with cosine distance is used for
item-to-item collaborative recommendation.

### 3. Hybrid Recommendation

The final system combines both recommendation signals.

```text
Hybrid Score =
0.3 × Content Score +
0.7 × Collaborative Score