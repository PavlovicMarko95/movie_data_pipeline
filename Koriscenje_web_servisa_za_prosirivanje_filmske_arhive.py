import pandas as pd
import requests
import xml.etree.ElementTree as ET
import time
from urllib.parse import quote

API_KEY = "VAS_API_KEY"

df = pd.read_csv("movies.csv")

def get_movie(title):
    #print(f"Pokusavam {title}...")
    safe_title = quote(str(title))
    url = f"http://www.omdbapi.com/?t={safe_title}&apikey={API_KEY}"

    try:
        data = requests.get(url).json()
        if data.get("Response") == "True":
            # obrada rejtinga
            rating = data.get("imdbRating", "0")
            votes = data.get("imdbVotes", "0").replace(",","")
            return (
                float(rating) if rating != "N/A" else 0.0,
                int(votes) if votes.isdigit() else 0,
                data.get("Actors", "N/A")
            )
    except Exception as e:
        print(f"Greska pri zahtevu: {e}")

    return 0.0, 0, "N/A"

results = []
for title in df["title"]:
    results.append(get_movie(title))
    time.sleep(0.2)

df[["imdbRating", "imdbVotes", "Actors"]] = results

top10 = df.sort_values(by="imdbRating", ascending=False).head(10)

top10.to_xml("Top10_movies.xml", parser="etree", index=False, root_name="movies", row_name="movie")

print("Top 10 XML fajl uspesno kreiran!")