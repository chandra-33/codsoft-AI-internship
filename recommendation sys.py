import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = {
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Pulp Fiction'],
    'Genre': ['Action Sci-Fi', 'Action Sci-Fi', 'Adventure Sci-Fi', 'Action Crime', 'Crime Drama']
}
df = pd.DataFrame(data)
print("Dataset:")
print(df)
tfidf = TfidfVectorizer(stop_words='english')
genre_matrix = tfidf.fit_transform(df['Genre'])
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)
def recommend_movies(movie_title, num_recommendations=3):
    idx = df[df['Title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]
    movie_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[movie_indices]
selected_movie = 'Inception'
print(f"\nRecommendations for '{selected_movie}':")
recommended_movies = recommend_movies(selected_movie)
print(recommended_movies.to_string(index=False))
