# movie_data_pipeline
## Features
- **Extract:** Reads movie titles from a `movies.csv` file.
- **Transform:** Fetches real-time ratings and cast info via **REST API**, handles missing values, and filters the Top 10 movies.
- **Load:** Exports the processed results into a structured **XML** format.

## Technologies
- Python 3.x
- Pandas library
- OMDb API

## How to Run
1. Clone the repository.
2. Replace `VAS_API_KEY` in the script with your [OMDb API key](http://www.omdbapi.com/apikey.aspx).
3. Ensure `movies.csv` is in the same folder.
4. Run the script: `Koriscenje_web_servisa_za_prosirivanje_filmske_arhive.py`
