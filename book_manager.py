import json


def show_avg_books():
    with open("books.json", "r") as f:
        data = json.load(f)
        for book in data["books"]:
            rating_scores = book["ratings"]
            avg_rating = round(sum(rating_scores) / len(rating_scores), 2)
            print(f"Book: {book['title']} , Avg rating: {avg_rating}")


def adding_book():
    with open("books.json", "r") as f:
        data = json.load(f)
        max_id = len(data["books"])
        new_book = {
            "id": max_id + 1,
            "title": "Earth",
            "author": "John Doe",
            "ratings": [3, 4, 3],
        }

        if any(
            book["title"].casefold() == new_book["title"].casefold()
            for book in data["books"]
        ):
            print(f"Book '{new_book['title']}' already exists")
            return
        data["books"].append(new_book)
        with open("books.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"Book '{new_book['title']}' added successfully.")
        return


def adding_category():
    print("Adding categories to each book... ")
    with open("books.json", "r+") as f:
        data = json.load(f)
        for book in data["books"]:
            if "python" in book["title"].casefold():
                book["category"] = "Programming"
            elif "javascript" in book["title"].casefold():
                book["category"] = "Web Development"
            else:
                book["category"] = "Other"

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        return


show_avg_books()
adding_book()
adding_category()
