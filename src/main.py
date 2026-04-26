from extractor import extract
from transformer import transform
from load import save_to_xml
from analysis import sort_movies_by_rating

# Extract data from CSV
csv_data = extract()

# Transform data by enriching it with OMDb API
movies = transform(csv_data)

# Load data into the xml file
save_to_xml(movies)

# Sort movies by IMDb rating and display top 10
sort_movies_by_rating(movies)
