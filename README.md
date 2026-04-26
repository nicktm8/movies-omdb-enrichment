# 🎬 Movies OMDb Enrichment

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Requests](https://img.shields.io/badge/Requests-2.0+-FF6B35?style=flat&logo=python&logoColor=white)](https://requests.readthedocs.io/)
[![OMDb API](https://img.shields.io/badge/OMDb-API-F5C518?style=flat&logo=imdb&logoColor=black)](https://www.omdbapi.com/)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)](https://github.com/nicktm8/movies-omdb-enrichment)

An ETL pipeline that enriches a movie dataset with live IMDb data fetched from the OMDb API — adding ratings, cast, and vote counts — and exports the full enriched dataset to XML.

---

## ⚙️ Features

- Extracts movie data from a CSV source file
- Fetches IMDb rating, main cast, and vote count for each film via the OMDb API
- Handles API errors, timeouts, and missing data gracefully
- Integrates enriched data back into the original dataset
- Exports the full enriched dataset to a structured XML file
- Displays the top 10 highest-rated films by IMDb score

---

## 🏗️ Project Structure

```
movies-omdb-enrichment/
│
├── data/
│   └── movies.csv                  # Input dataset
│
├── output/
│   └── movies_enriched.xml         # Enriched output (auto-created)
│
├── src/
│   ├── main.py                     # Pipeline entry point
│   ├── config.py                   # Centralized configuration (paths, API key)
│   ├── extractor.py                # CSV ingestion and column normalization
│   ├── omdb_client.py              # OMDb API communication and error handling
│   ├── transformer.py              # Data enrichment and type conversion
│   ├── load.py                     # XML export
│   └── analysis.py                 # Sorting and top 10 display
│
├── config.example.py               # Safe config template (no secrets)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- OMDb API key — register for free at [omdbapi.com](https://www.omdbapi.com/)

### Installation

1. Clone the repository:

```
git clone https://github.com/nicktm8/movies-omdb-enrichment.git
cd movies-omdb-enrichment
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Set up your config:

```
cp config.example.py src/config.py
```

Then open `src/config.py` and add your OMDb API key.

4. Run the pipeline:

```
cd src
python main.py
```

---

## 📊 Output

### XML Export

The enriched dataset is saved to `output/movies_enriched.xml` with the following structure:

```xml
<movies>
  <movie title="The Dark Knight">
    <year>2008</year>
    <genre>Action, Crime, Drama</genre>
    <director>Christopher Nolan</director>
    <country>USA</country>
    <duration>152</duration>
    <imdb_rating>9.0</imdb_rating>
    <actors>Christian Bale, Heath Ledger, Aaron Eckhart</actors>
    <imdb_votes>2,800,000</imdb_votes>
  </movie>
  ...
</movies>
```

### Top 10 Console Output

```
--- TOP 10 movies by IMDb rating ---
1. The Shawshank Redemption (1994) - IMDb Rating: 9.3
2. The Godfather (1972) - IMDb Rating: 9.2
3. The Dark Knight (2008) - IMDb Rating: 9.0
...
```

---

## 🧱 Architecture

The pipeline follows a strict **ETL (Extract → Transform → Load)** pattern extended with a dedicated API client and analysis layer:

| Layer | File | Responsibility |
| --- | --- | --- |
| Extract | `extractor.py` | Read CSV, normalize column names |
| API Client | `omdb_client.py` | HTTP requests to OMDb, error handling |
| Transform | `transformer.py` | Enrich each row with API data, type conversion |
| Load | `load.py` | Export enriched dataset to XML |
| Analysis | `analysis.py` | Sort by IMDb rating, display top 10 |
| Config | `config.py` | Centralized paths and API key |
| Entry point | `main.py` | Orchestrate the full pipeline |

**Data flow:**

```
movies.csv → extractor.py → transformer.py ↔ omdb_client.py → load.py → movies_enriched.xml
                                                                    ↓
                                                             analysis.py → console
```

---

## 🛡️ Error Handling

The pipeline handles failures at two levels:

- **Network errors** — `requests.exceptions.Timeout`, `ConnectionError`, and non-200 HTTP responses are caught per film; the pipeline continues without interruption
- **API errors** — OMDb returns `"Response": "False"` when a film is not found; missing fields fall back to `0.0` (rating) or `"N/A"` (text fields)

No single failed API call stops the pipeline.

---

## 🛠️ Planned Improvements

- Replace `print()` statements with Python `logging` module
- Add retry logic for failed API requests
- Add unit tests for `transformer.py` and `omdb_client.py`
- Support additional output formats (CSV, JSON)
- Add a summary report: total enriched, total failed, average IMDb rating

---

## 🧠 Technical Highlights

- **ETL architecture** — strict separation between extraction, transformation, loading, and analysis
- **Dedicated API client** — `omdb_client.py` isolates all HTTP logic; the transformer never touches `requests` directly
- **Type safety** — `imdb_rating` is converted to `float` at transform time, preventing silent sort errors
- **Graceful degradation** — failed API lookups fall back to `0.0` / `"N/A"` so the pipeline always produces a complete output file
- **GitHub-safe config** — API key lives in `config.py` (gitignored); `config.example.py` is committed as a safe template

---

## Changelog

### v1.0.0 — Initial Release

- Add `extractor.py` for CSV ingestion and column normalization
- Add `omdb_client.py` for OMDb API communication with error handling
- Add `transformer.py` for data enrichment and float type conversion
- Add `load.py` for XML export using pandas `.to_xml()`
- Add `analysis.py` for sorting and top 10 display
- Add `config.py` with centralized paths and API key setup
- Add `config.example.py` as a GitHub-safe config template

---

## Contributing

Contributions, suggestions, and feedback are welcome.

1. Fork the repository
2. Create a new branch:

```
git checkout -b feature/your-feature-name
```

3. Commit your changes:

```
git commit -m "feat: add your feature"
```

4. Push to your branch:

```
git push origin feature/your-feature-name
```

5. Open a Pull Request

If you spot a bug or have an idea, feel free to open an [issue](https://github.com/nicktm8/movies-omdb-enrichment/issues).

---

## 👤 Author

Nick Tem
GitHub: https://github.com/nicktm8