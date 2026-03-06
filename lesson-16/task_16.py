# homework_pandas.py

import pandas as pd
import sqlite3

# =========================
# Part 1: Reading Files
# =========================

print("\n--- PART 1: READING FILES ---")

# 1. chinook.db
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql("SELECT * FROM customers", conn)
print("\nCustomers (first 10 rows):")
print(customers_df.head(10))
conn.close()

# 2. iris.json
iris_df = pd.read_json("iris.json")
print("\nIris shape:", iris_df.shape)
print("Iris columns:", iris_df.columns.tolist())

# 3. titanic.xlsx
titanic_df = pd.read_excel("titanic.xlsx")
print("\nTitanic (first 5 rows):")
print(titanic_df.head())

# 4. Flights parquet file
flights_df = pd.read_parquet("flights.parquet")
print("\nFlights info:")
print(flights_df.info())

# 5. movie.csv
movie_df = pd.read_csv("movie.csv")
print("\nMovie random sample (10 rows):")
print(movie_df.sample(10))


# =========================
# Part 2: Exploring DataFrames
# =========================

print("\n--- PART 2: EXPLORING DATAFRAMES ---")

# 1. iris.json
iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[["sepal_length", "sepal_width"]]
print("\nIris selected columns:")
print(iris_selected.head())

# 2. titanic.xlsx
titanic_over_30 = titanic_df[titanic_df["Age"] > 30]
print("\nTitanic passengers over age 30 (first 5):")
print(titanic_over_30.head())

print("\nTitanic gender counts:")
print(titanic_df["Sex"].value_counts())

# 3. Flights parquet file
flights_subset = flights_df[["origin", "dest", "carrier"]]
print("\nFlights subset (first 5):")
print(flights_subset.head())

print("\nNumber of unique destinations:")
print(flights_df["dest"].nunique())

# 4. movie.csv
long_movies = movie_df[movie_df["duration"] > 120]
long_movies_sorted = long_movies.sort_values(
    by="director_facebook_likes",
    ascending=False
)

print("\nLong movies sorted by director_facebook_likes:")
print(long_movies_sorted.head())


# =========================
# Part 3: Challenges & Explorations
# =========================

print("\n--- PART 3: CHALLENGES ---")

# Iris statistics
print("\nIris statistics (mean, median, std):")
print(iris_df.agg(["mean", "median", "std"]))

# Titanic age stats
print("\nTitanic age stats (min, max, sum):")
print(titanic_df["Age"].agg(["min", "max", "sum"]))

# Movie.csv challenges
director_likes = (
    movie_df.groupby("director_name")["director_facebook_likes"]
    .sum()
    .sort_values(ascending=False)
)

print("\nDirector with highest total Facebook likes:")
print(director_likes.head(1))

print("\n5 longest movies and directors:")
print(
    movie_df[["movie_title", "director_name", "duration"]]
    .sort_values(by="duration", ascending=False)
    .head(5)
)

# Flights parquet missing values
print("\nMissing values in flights dataset:")
print(flights_df.isna().sum())

# Fill missing values in a numerical column (example: dep_delay)
if "dep_delay" in flights_df.columns:
    flights_df["dep_delay"] = flights_df["dep_delay"].fillna(
        flights_df["dep_delay"].mean()
    )
    print("\nMissing dep_delay values filled with mean.")
else:
    print("\nColumn 'dep_delay' not found in flights dataset.")
