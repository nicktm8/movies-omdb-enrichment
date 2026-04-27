import pandas as pd
from config import INPUT_FILE

def extract(file_path=INPUT_FILE):
    try:
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.strip().str.lower()
        data = data.rename(columns={"release_year": "year"})
        
        print(f"\n✅ Loaded {len(data)} movies from '{file_path}'")
        print("-----------------------------")
        
        return data
    
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        raise
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        raise
