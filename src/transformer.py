from omdb_client import get_movie_data



def transform(csv_data):
    movies = []
    
    
    for _, row in csv_data.iterrows():
        title = row['title']
        year = row['year']
        
        omdb_data = get_movie_data(title, year)
        
        if omdb_data is not None:
            row['imdb_rating'] = omdb_data['imdb_rating']
            row['actors'] = omdb_data['actors']
            row['imdb_votes'] = omdb_data['imdb_votes']

            print(f"✅ Enriched: {title} ({year})")
            print("-----------------------------")
        else:
            row["imdb_rating"] = "N/A"
            row["actors"] = "N/A"
            row["imdb_votes"] = "N/A"
        
        print("-----------------------------")
        movies.append(row)
    
    return movies
