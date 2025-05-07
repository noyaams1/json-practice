import json

filename = "./movies.json"


# function to load data from JSON file ===
def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


# function to Save data back to the JSON file
def save_data(movies_data, filename):
    with open(filename, "w") as file:
        json.dump(movies_data, file, indent=4)


# searching a movie by title
def search_movie(movies_data, movie_title):
    for movie in movies_data["movies"]:
        if movie_title.casefold() == movie["title"].casefold():
            return movie  # Return the movie if found
    return None  # Return None if not found


# adding a new movie & updating data
def add_movie(movies_data, new_movie):
    if search_movie(movies_data, new_movie["title"]):
        print(f"Movie '{new_movie['title']}' already exists.")
        return
    max_id = max((movie["id"] for movie in movies_data["movies"]), default=0)
    new_movie["id"] = max_id + 1
    movies_data["movies"].append(new_movie)
    save_data(movies_data, filename)
    print(f"Movie '{new_movie['title']}' added successfully.")


# top movies and genre counts report
def movies_report(movies_data):
    print("\n🎬 Top 3 Movies by Rating:")
    top_movies = sorted(movies_data["movies"], key=lambda m: m["rating"], reverse=True)[
        :3
    ]
    for movie in top_movies:
        print(f"- {movie['title']} ({movie['rating']})")

    print("\n📊 Movies per Genre:")
    genre_counts = {}
    for movie in movies_data["movies"]:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1  # counting occurrences
    for genre, count in genre_counts.items():
        print(f"- {genre}: {count}")


new_movie = {
    "title": "Inception",
    "director": "Chris-Columbus",
    "rating": 10,
    "genres": ["Sci-Fi"],
}


def main():
    movies_data = load_data(filename)  # Step 1: Load data

    movie_title = input("Enter the title of the movie you search: ").strip()
    movie = search_movie(movies_data, movie_title)
    # Step 2: Ask user to search for a movie
    if movie:
        print(f"Movie found: {movie}")
    else:
        print("Movie not found.")

    # Step 3: Add or update a predefined movie (new_movie)
    found = search_movie(movies_data, new_movie["title"])
    if found:
        old_rating = found["rating"]
        found["rating"] = new_movie["rating"]
        print(
            f"Updated '{found['title']}' rating from {old_rating} to {new_movie['rating']}"
        )
    else:
        add_movie(movies_data, new_movie)
    # Step 4: Save the final state
    save_data(movies_data, filename)
    # Step 5: Print a report summary
    movies_report(movies_data)


main()
