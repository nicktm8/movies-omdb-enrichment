
def sort_movies_by_rating(movies):
    sorted_movies = movies.sort_values(by='imdb_rating', ascending=False)
    
    print("\n--- TOP 10 movies by IMDb rating ---\n")
    
    for i, (_, movie) in enumerate(sorted_movies.head(10).iterrows(), start=1):
        print(f"{i}. {movie['title']} ({movie['year']}) - IMDb Rating: {movie['imdb_rating']}")

    return sorted_movies
