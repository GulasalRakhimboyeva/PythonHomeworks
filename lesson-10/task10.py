# ## Task 1: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the `requests` library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

# ## Task 2: Movie Recommendation System
#    1. Use this url https://developer.themoviedb.org/docs/getting-started/ to fetch information about movies.
#    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.


import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"
CITY = "Tashkent"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"  # Celsius
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
else:
    print("Error fetching weather data:", response.status_code)

import requests
import random

API_KEY = "YOUR_TMDB_API_KEY"
BASE_URL = "https://api.themoviedb.org/3"

# Step 1: Get available genres
genre_url = f"{BASE_URL}/genre/movie/list"
params = {"api_key": API_KEY}

genre_response = requests.get(genre_url, params=params)
genres = genre_response.json()["genres"]

# Create a dictionary: genre name -> genre id
genre_dict = {genre["name"].lower(): genre["id"] for genre in genres}

# Step 2: Ask user for genre
user_genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").lower()

if user_genre not in genre_dict:
    print("Genre not found. Available genres are:")
    for g in genre_dict:
        print("-", g.title())
else:
    genre_id = genre_dict[user_genre]

    # Step 3: Discover movies by genre
    discover_url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id
    }

    movie_response = requests.get(discover_url, params=params)
    movies = movie_response.json()["results"]

    if movies:
        movie = random.choice(movies)
        print("\n🎥 Recommended Movie:")
        print("Title:", movie["title"])
        print("Release Date:", movie["release_date"])
        print("Overview:", movie["overview"])
    else:
        print("No movies found for this genre.")
