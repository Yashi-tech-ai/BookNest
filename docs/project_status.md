# BookNest — Project Status

## Project Overview

BookNest is a book recommendation system built using the Goodreads
dataset. The system combines content-based filtering and
collaborative filtering into a hybrid recommendation system.

The final project will be presented as a web application.

---

## Current Project Structure

```text
BookNest/
├── Data/
│   ├── books.csv
│   ├── ratings.csv
│   ├── tags.csv
│   ├── book_tags.csv
│   ├── to_read.csv
│   └── books_features.csv
│
├── docs/
├── experiments/
│   └── hybrid_experiments.csv
│
├── models/
├── Notebooks/
│   ├── 01_dataset_audit.ipynb
│   ├── 02_dataset_preprocessing.ipynb
│   ├── 03_recommendation_model.ipynb
│   └── 04_evaluation.ipynb
│
├── src/
└── tests/




---

## Evaluation Status

The recommendation system has been evaluated using a leave-one-out
item-to-item retrieval approach.

### Evaluation Setup

- Evaluation cases: 1,000
- Unique seed books: 813
- Recommendation list sizes: K = 5, 10, 20
- Hybrid configurations tested: 6
- Alpha values tested: 0.3, 0.4, 0.5, 0.6, 0.7, 0.8
- Metrics: Precision@10, Recall@10, Hit Rate@5, Hit Rate@10, Hit Rate@20

### Baseline Results

| K | Content Hit Rate | Collaborative Hit Rate |
|---|---:|---:|
| 5 | 0.019 | 0.023 |
| 10 | 0.025 | 0.043 |
| 20 | 0.042 | 0.043 |

### Hybrid Results

| Alpha | Content Weight | Collaborative Weight | Hit Rate@5 | Hit Rate@10 | Hit Rate@20 |
|---:|---:|---:|---:|---:|---:|
| 0.8 | 0.8 | 0.2 | 0.018 | 0.029 | 0.042 |
| 0.7 | 0.7 | 0.3 | 0.018 | 0.032 | 0.045 |
| 0.6 | 0.6 | 0.4 | 0.019 | 0.036 | 0.049 |
| 0.5 | 0.5 | 0.5 | 0.022 | 0.039 | 0.051 |
| 0.4 | 0.4 | 0.6 | 0.022 | 0.040 | 0.053 |
| 0.3 | 0.3 | 0.7 | 0.023 | 0.042 | 0.053 |

### Evaluation Findings

- Collaborative filtering performed better than content-based filtering
  on the evaluated dataset.
- Among the tested hybrid configurations, alpha = 0.3 performed best
  at K = 5 and K = 10.
- At K = 20, alpha = 0.3 and alpha = 0.4 achieved the highest hybrid
  Hit Rate of 0.053.
- The pure collaborative model achieved a slightly higher Hit Rate@10
  (0.043) than the best hybrid configuration (0.042).
- The hybrid model achieved a higher Hit Rate@20 (0.053) than the pure
  collaborative baseline (0.043).

### Current Conclusion

The evaluation indicates that collaborative filtering provides the
strongest recommendation signal for this dataset. A collaborative-heavy
hybrid configuration is competitive, with alpha = 0.3 being the
strongest tested hybrid configuration overall.

---

## Next Stage

Finalize the evaluation results and determine the configuration to use
for the final BookNest recommendation system before proceeding to
application development.


---

## Final Model Configuration

The final BookNest hybrid recommendation configuration has been selected
based on the evaluation experiments.

- Final content weight (alpha): 0.3
- Final collaborative weight: 0.7
- Final recommendation count (K): 10

The hybrid recommender uses:

Hybrid Score = 0.3 × Content Score + 0.7 × Collaborative Score

The final configuration is a collaborative-heavy hybrid recommender.




## Production Code Refactoring

The finalized recommendation logic from `03_recommendation_model.ipynb`
has been extracted into reusable Python modules under `src/`.

Production modules:

- `src/content_recommender.py`
- `src/collaborative_recommender.py`
- `src/hybrid_recommender.py`

The data-loading paths were updated to use project-relative paths so the
modules work independently of the notebook working directory.

Automated tests were added in:

- `tests/test_recommenders.py`

The test suite verifies:

- Content-based recommender returns 10 recommendations.
- Collaborative recommender returns 10 recommendations.
- Hybrid recommender returns 10 recommendations.
- The seed book is excluded from recommendations.
- Hybrid scores follow the final formula:
  `0.3 × content_score + 0.7 × collaborative_score`

Test result:

- **4/4 tests passed**