import pandas as pd

def extract(file_path):
    try:
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.strip().str.lower()
        data = data.rename(columns={"release_year": "year"})
        print(f"✅ Loaded {len(data)} movies from '{file_path}'")
    
        return data
    
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        raise
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        raise
