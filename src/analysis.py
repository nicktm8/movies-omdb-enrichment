
def sort_movies_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda x: x['imdb_rating'], reverse=True)
    
    print("\n--- TOP 10 movies by IMDb rating ---")
    
    for i, movie in enumerate(sorted_movies[:10], start=1):
                print(f"{i}. {movie['title']} ({movie['year']}) - IMDb Rating: {movie['imdb_rating']}")

    return sorted_movies
