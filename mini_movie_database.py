import json

filename = "./movies.json"


def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


def save_data(movies_data, filename):
    with open(filename, "w") as file:
        json.dump(movies_data, file, indent=4)


def search_movie(movies_data, movie_title):
    for movie in movies_data["movies"]:
        if movie_title.casefold() == movie["title"].casefold():
            return movie
    return None


def add_movie(movies_data, new_movie):
    if search_movie(movies_data, new_movie["title"]):
        print(f"Movie '{new_movie['title']}' already exists.")
        return
    max_id = max((movie["id"] for movie in movies_data["movies"]), default=0)
    new_movie["id"] = max_id + 1
    movies_data["movies"].append(new_movie)
    save_data(movies_data, filename)
    print(f"Movie '{new_movie['title']}' added successfully.")


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
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    for genre, count in genre_counts.items():
        print(f"- {genre}: {count}")


new_movie = {
    "title": "Inception",
    "director": "Chris-Columbus",
    "rating": 10,
    "genres": ["Sci-Fi"],
}


def main():
    movies_data = load_data(filename)

    movie_title = input("Enter the title of the movie you search: ").strip()
    movie = search_movie(movies_data, movie_title)

    if movie:
        print(f"Movie found: {movie}")
    else:
        print("Movie not found.")

    found = search_movie(movies_data, new_movie["title"])
    if found:
        old_rating = found["rating"]
        found["rating"] = new_movie["rating"]
        print(
            f"Updated '{found['title']}' rating from {old_rating} to {new_movie['rating']}"
        )
    else:
        add_movie(movies_data, new_movie)

    save_data(movies_data, filename)
    movies_report(movies_data)


main()
