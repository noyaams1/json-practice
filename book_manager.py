import json


# display each book's title and its average rating
def show_avg_books():
    with open("books.json", "r") as f:
        data = json.load(f)
        for book in data["books"]:
            rating_scores = book["ratings"]
            avg_rating = round(sum(rating_scores) / len(rating_scores), 2)
            print(f"Book: {book['title']} , Avg rating: {avg_rating}")


# adding a new book to the data
def adding_book():
    with open("books.json", "r") as f:
        data = json.load(f)
        max_id = len(data["books"])
        # defining new book details
        new_book = {
            "id": max_id + 1,
            "title": "Harry Potter",
            "author": "J. K. Rowling",
            "ratings": [5, 4, 5],
        }
        # checking for duplicate title (case-insensitive)
        if any(
            book["title"].casefold() == new_book["title"].casefold()
            for book in data["books"]
        ):
            print(f"Book '{new_book['title']}' already exists")
            return
        # adding new book & updating data
        data["books"].append(new_book)
        with open("books.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"Book '{new_book['title']}' added successfully.")
        return


# adding a category to each book based on the title
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

        f.seek(0)  # Move file pointer to start before writing
        json.dump(data, f, indent=4)  # Write updated data to file
        f.truncate()  # Remove any leftover data after the new JSON
        return


show_avg_books()
adding_book()
adding_category()
