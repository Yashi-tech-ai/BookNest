# BookNest – Hybrid Book Recommendation System

A personalized book recommendation system built using hybrid recommendation techniques and presented through an interactive Streamlit web application.

---

## Project Overview

BookNest is a book recommendation system developed using the Goodbooks-10k dataset.

The project combines content-based filtering and collaborative filtering to generate personalized book recommendations. By integrating both approaches, the system considers book similarities as well as user rating patterns.

The final application allows users to select a book and receive 10 recommended books through an interactive Streamlit interface.

## Recommendation Approach

BookNest uses three recommendation approaches:

### 1. Content-Based Filtering

Content-based filtering recommends books based on their similarity to a selected book.

- Uses book metadata and tags to represent book characteristics.
- TF-IDF vectorization converts textual information into numerical representations.
- Cosine similarity measures the similarity between books.

### 2. Collaborative Filtering

Collaborative filtering identifies books with similar rating patterns.

- Uses the ratings dataset to understand user preferences.
- Applies a K-Nearest Neighbors (KNN) approach.
- Uses cosine distance to identify similar books based on rating patterns.
- Generates recommendations based on item-to-item similarity.

### 3. Hybrid Recommendation

The final recommendation system combines content-based and collaborative filtering scores using a weighted approach.

**Hybrid Score:**

```text
Hybrid Score =
0.3 × Content Score +
0.7 × Collaborative Score
```

The collaborative filtering component receives a higher weight, while content-based filtering contributes additional information about book similarity.

The system combines both scores to generate the final ranked recommendations.

## Dataset

**Dataset:** Goodbooks-10k

**Source:** Publicly available Goodbooks-10k dataset.

The dataset contains information about books, user ratings, tags, and book-related metadata.

The project primarily uses:
- Books dataset – book titles, authors, and other metadata.
- Ratings dataset – user ratings for different books.
- Tags and book-tag data – information used for content-based recommendations.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- SciPy
- Jupyter Notebook

## System Workflow

1. **Data Loading:** Load the Goodbooks-10k dataset, including book metadata, ratings, and tags.

2. **Data Preprocessing:** Clean and prepare the datasets for recommendation modelling.

3. **Content-Based Filtering:** Apply TF-IDF vectorization and cosine similarity to identify books with similar metadata and tags.

4. **Collaborative Filtering:** Construct a book-rating representation and apply KNN with cosine distance to identify similar books.

5. **Hybrid Recommendation:** Combine the content-based and collaborative filtering scores using weighted scoring.

6. **Ranking:** Rank the candidate books according to their final hybrid scores.

7. **Recommendation Display:** Present the top 10 recommended books through the Streamlit web application.

## Web Application

BookNest uses Streamlit to provide an interactive interface.

Users can:
- Select a book from the available collection.
- Generate recommendations based on the selected book.
- View the top 10 recommended books.

The application makes the recommendation system accessible without requiring users to interact directly with the underlying machine learning code.

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/Yashi-tech-ai/BookNest.git
cd BookNest
```

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install pandas numpy scikit-learn streamlit scipy
```

### 3. Run the Application

Navigate to the project directory and execute:

```bash
streamlit run app.py
```


## Key Features

- Hybrid recommendation combining content-based and collaborative filtering.
- TF-IDF-based textual similarity.
- Item-to-item collaborative filtering using KNN.
- Weighted combination of recommendation scores.
- Interactive Streamlit interface.
- Top 10 book recommendations for a selected book.

## Limitations

- Recommendation quality depends on the availability and quality of book metadata and user ratings.
- Books with limited rating information may receive less effective collaborative recommendations.
- The system is based on the available Goodbooks-10k dataset and may not reflect newer books or changing reader preferences.
- The recommendations are generated from a selected book rather than a complete user-specific reading history.

## Future Improvements

- Introduce user-specific recommendation profiles.
- Incorporate additional book metadata and descriptions.
- Experiment with different hybrid scoring weights.
- Improve recommendations for books with limited rating information.
- Deploy the application online for wider accessibility.

## Acknowledgements

The project uses the publicly available Goodbooks-10k dataset for developing and evaluating the recommendation system.