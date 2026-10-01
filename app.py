import streamlit as st
import pandas as pd

from src.hybrid_recommender import recommend_hybrid


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="BookNest",
    page_icon="📖",
    layout="wide"
)


# ============================================================
# CUSTOM FRONTEND DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       WARM LIBRARY BACKGROUND
       ====================================================== */

    .stApp {
        background-image:
            linear-gradient(
                rgba(57, 31, 18, 0.38),
                rgba(57, 31, 18, 0.52)
            ),
            url("https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=2200&q=90");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }


    /* ======================================================
       MAIN CONTENT PANEL
       ====================================================== */

    .block-container {
        max-width: 1150px;

        margin-top: 2rem;
        margin-bottom: 3rem;

        padding: 2.8rem 4rem 4rem 4rem;

        background:
            rgba(244, 228, 202, 0.975);

        border-radius: 24px;

        border:
            1px solid rgba(255, 239, 211, 0.9);

        box-shadow:
            0 18px 50px rgba(35, 18, 8, 0.42);

        /* IMPORTANT:
           Makes the doodles stay inside this panel */
        position: relative;
    }


    /* ======================================================
       SIDE DOODLES
       Decorative only — does NOT affect any widgets
       ====================================================== */

    .block-container::before {
        content:
            "✦  ❧  ✧\\A"
            "❦     ✦\\A"
            "⌁  ❧  ✦";

        white-space: pre;

        position: absolute;

        left: 42px;
        top: 70px;

        color: #a8754e;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 1.15rem;

        line-height: 2.1;

        opacity: 0.62;

        pointer-events: none;

        z-index: 0;
    }


    .block-container::after {
        content:
            "✧  ❧  ✦\\A"
            "✦     ❦\\A"
            "❧  ⌁  ✧";

        white-space: pre;

        position: absolute;

        right: 42px;
        top: 70px;

        color: #a8754e;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 1.15rem;

        line-height: 2.1;

        opacity: 0.62;

        pointer-events: none;

        z-index: 0;
    }


    /* ======================================================
       BOOKNEST TITLE
       ====================================================== */

    h1 {
        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        font-size: 4.2rem !important;

        font-weight: 700 !important;

        text-align: center;

        color: #422417 !important;

        letter-spacing: 0.5px;

        margin-top: 0 !important;

        margin-bottom: 0.2rem !important;

        text-shadow:
            0 1px 1px rgba(255, 245, 225, 0.7);
    }


    /* ======================================================
       SUBTITLE
       ====================================================== */

    .booknest-subtitle {
        text-align: center;

        color: #76543c;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 1.08rem;

        font-style: italic;

        margin-bottom: 1rem;
    }


    /* ======================================================
       HERO DECORATION
       ====================================================== */

    .hero-decoration {

        display: flex;

        align-items: center;

        justify-content: center;

        gap: 14px;

        margin:
            0.7rem auto 0.8rem auto;

        color: #a06b43;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 1.05rem;
    }


    .hero-line {

        width: 125px;

        height: 1px;

        background:
            #c9aa88;
    }


    .hero-symbol {
        font-size: 1.1rem;

        color:
            #9b633d;
    }


    /* ======================================================
       HERO MESSAGE
       ====================================================== */

    .hero-message {

        max-width: 700px;

        margin:
            0 auto 1.2rem auto;

        text-align: center;

        color:
            #654834;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size:
            0.94rem;

        line-height:
            1.65;
    }


    /* ======================================================
       LIBRARY TAGS
       ====================================================== */

    .library-tags {

        display: flex;

        justify-content: center;

        gap: 12px;

        margin:
            1.1rem 0 2.3rem 0;

        flex-wrap: wrap;
    }


    .library-tag {

        padding:
            0.38rem 1rem;

        border:
            1px solid #c9aa88;

        border-radius:
            20px;

        color:
            #79543a;

        background:
            rgba(255, 248, 235, 0.58);

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size:
            0.78rem;

        letter-spacing:
            0.5px;
    }


    /* ======================================================
       LITERARY QUOTE
       ====================================================== */

    .literary-quote {

        max-width:
            720px;

        margin:
            0 auto 1.7rem auto;

        padding:
            0.85rem 2rem;

        text-align:
            center;

        color:
            #6b4a35;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size:
            0.98rem;

        font-style:
            italic;

        line-height:
            1.6;

        border-top:
            1px solid #c9aa88;

        border-bottom:
            1px solid #c9aa88;
    }


    .quote-author {

        display:
            block;

        margin-top:
            0.25rem;

        font-size:
            0.8rem;

        font-style:
            normal;

        color:
            #896b51;
    }


    /* ======================================================
       DECORATIVE SECTION LABEL
       ====================================================== */

    .library-label {

        text-align:
            center;

        color:
            #a06b43;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size:
            0.78rem;

        text-transform:
            uppercase;

        letter-spacing:
            3px;

        margin-bottom:
            0.8rem;
    }


    /* ======================================================
       SECTION HEADINGS
       ====================================================== */

    h2 {

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        color:
            #4b2919 !important;

        font-weight:
            700 !important;

        font-size:
            1.85rem !important;
    }


    h3 {

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        color:
            #4b2919 !important;

        font-weight:
            700 !important;
    }


    /* ======================================================
       NORMAL TEXT
       ====================================================== */

    p {
        color:
            #4d3628;
    }


    /* ======================================================
       SELECT BOX
       ====================================================== */

    div[data-baseweb="select"] > div {

        background-color:
            #fff8eb !important;

        border:
            1px solid #bfa487 !important;

        border-radius:
            12px !important;

        min-height:
            48px;

        box-shadow:
            inset 0 1px 2px rgba(100, 55, 25, 0.05);
    }


    div[data-baseweb="select"] * {
        color:
            #4a2d1d !important;
    }


    /* ======================================================
       RECOMMENDATION BUTTON
       ====================================================== */

    .stButton > button {

        background:
            linear-gradient(
                135deg,
                #9a5b37,
                #774025
            ) !important;

        color:
            #fff8ed !important;

        border:
            none !important;

        border-radius:
            12px !important;

        min-height:
            48px;

        padding:
            0.7rem 1.5rem;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size:
            1.05rem;

        font-weight:
            600;

        box-shadow:
            0 5px 14px rgba(86, 42, 20, 0.25);

        transition:
            all 0.2s ease;
    }


    .stButton > button:hover {

        background:
            linear-gradient(
                135deg,
                #854a2d,
                #62321e
            ) !important;

        color:
            white !important;

        transform:
            translateY(-2px);

        box-shadow:
            0 8px 18px rgba(86, 42, 20, 0.32);
    }


    /* ======================================================
       RECOMMENDATION CARDS
       ====================================================== */

    div[data-testid="stHorizontalBlock"] {

        background:
            #fff9ef;

        border:
            1px solid #dcc6aa;

        border-radius:
            18px;

        padding:
            1.25rem;

        margin-top:
            0.8rem;

        margin-bottom:
            0.8rem;

        box-shadow:
            0 5px 16px rgba(82, 47, 26, 0.10);
    }


    /* ======================================================
       BOOK TITLES
       ====================================================== */

    div[data-testid="stHorizontalBlock"] h3 {

        color:
            #4a2819 !important;

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        font-size:
            1.4rem !important;

        line-height:
            1.35;
    }


    /* ======================================================
       BOOK INFORMATION
       ====================================================== */

    div[data-testid="stHorizontalBlock"] p {

        color:
            #624635 !important;

        font-size:
            0.98rem;
    }


    /* ======================================================
       DIVIDERS
       ====================================================== */

    hr {

        border:
            none !important;

        border-top:
            1px solid #d3b99b !important;

        margin-top:
            1.4rem !important;

        margin-bottom:
            1.4rem !important;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    .booknest-footer {

        text-align:
            center;

        color:
            #f4dfc1;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size:
            0.9rem;

        font-style:
            italic;

        margin-top:
            1.5rem;

        text-shadow:
            0 2px 8px rgba(0, 0, 0, 0.85);
    }


    /* ======================================================
       STREAMLIT CLEANUP
       ====================================================== */

    #MainMenu {
        visibility:
            hidden;
    }

    footer {
        visibility:
            hidden;
    }

    header {
        background:
            transparent !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD BOOK DATA
# ============================================================

books = pd.read_csv(
    "Data/books_features.csv"
)

book_titles = books["title"].tolist()


# ============================================================
# BOOKNEST HEADER
# ============================================================

st.title("BookNest")


st.markdown(
    """
    <div class="booknest-subtitle">
        A cozy corner for stories worth getting lost in.
    </div>

    <div class="hero-decoration">
        <span class="hero-line"></span>
        <span class="hero-symbol">✦</span>
        <span class="hero-symbol">✦</span>
        <span class="hero-symbol">✦</span>
        <span class="hero-line"></span>
    </div>

    <div class="hero-message">
        Step into your own little reading room.
        Choose a story that stayed with you,
        and let BookNest discover where your next
        chapter might take you.
    </div>

    <div class="library-tags">
        <span class="library-tag">READ</span>
        <span class="library-tag">DISCOVER</span>
        <span class="library-tag">GET LOST</span>
    </div>

    <div class="literary-quote">
        "Books are a uniquely portable magic."
        <span class="quote-author">
            — Stephen King
        </span>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# BOOK SELECTION
# ============================================================

st.markdown(
    """
    <div class="library-label">
        Your personal bookshelf
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader(
    "What are you in the mood for?"
)

st.write(
    "Choose a book you enjoyed, and BookNest will find "
    "your next reads."
)


selected_book = st.selectbox(
    "Choose a book:",
    book_titles
)


# ============================================================
# RECOMMENDATION BUTTON
# ============================================================

if st.button("✨ Find My Next Read"):

    # --------------------------------------------------------
    # EXISTING RECOMMENDER — DO NOT CHANGE
    # --------------------------------------------------------

    recommendations = recommend_hybrid(
        selected_book
    )


    # --------------------------------------------------------
    # ADD BOOK INFORMATION
    # --------------------------------------------------------

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


    # ========================================================
    # RECOMMENDATIONS HEADING
    # ========================================================

    st.markdown(
        """
        <div class="library-label">
            From the shelves
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader(
        "Your next reads"
    )

    st.write(
        "Books chosen especially for you from your selected title."
    )


    # ========================================================
    # DISPLAY RECOMMENDATIONS
    # ========================================================

    for _, book in recommendations.iterrows():

        col1, col2 = st.columns(
            [1, 4]
        )


        # ----------------------------------------------------
        # BOOK COVER
        # ----------------------------------------------------

        with col1:

            if pd.notna(
                book["image_url"]
            ):

                st.image(
                    book["image_url"],
                    width=140
                )


        # ----------------------------------------------------
        # BOOK INFORMATION
        # ----------------------------------------------------

        with col2:

            # Book title
            st.markdown(
                f"### {book['title']}"
            )


            # Author
            st.write(
                f"by {book['authors']}"
            )


            # Rating
            if pd.notna(
                book["average_rating"]
            ):

                st.write(
                    f"⭐ {book['average_rating']:.2f}"
                )


            # Publication year
            if pd.notna(
                book["original_publication_year"]
            ):

                st.write(
                    f"Published: "
                    f"{int(book['original_publication_year'])}"
                )


        st.divider()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="booknest-footer">
        There is always another story waiting.
    </div>
    """,
    unsafe_allow_html=True
)