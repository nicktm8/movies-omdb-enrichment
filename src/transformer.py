from omdb_client import get_movie_data

def transform(csv_data):
    result = []
    
    for _, row in csv_data.iterrows():
        title = row['title']
        year = row['year']
        
        omdb_data = get_movie_data(title, year)
        
        if omdb_data is not None:
            try:
                row['imdb_rating'] = float(omdb_data['imdb_rating'])
            except ValueError:
                row['imdb_rating'] = 0.0
                
            row['actors'] = omdb_data['actors']
            row['imdb_votes'] = omdb_data['imdb_votes']
   
        else:
            row["imdb_rating"] = 0.0
            row["actors"] = "N/A"
            row["imdb_votes"] = "N/A"
        
        result.append(row)
        print("-----------------------------")
        
    return result
