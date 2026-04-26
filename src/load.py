from config import OUTPUT_FILE
import pandas as pd

def save_to_xml(data, file_path=OUTPUT_FILE):
    try:
        df = pd.DataFrame(data)
        
        df.to_xml(
        file_path,
        parser='etree',
        root_name='movies',
        row_name='movie',
        index=False,
        attr_cols=['title'],
        elem_cols=['year', 'genre', 'director', 'country', 'duration', 'imdb_rating', 'actors', 'imdb_votes']
    )
        print(f"✅ Data successfully saved to '{file_path}'")
        print("================================")
        
    except Exception as e:
        print(f"❌ Error saving data to XML: {e}")
        raise
