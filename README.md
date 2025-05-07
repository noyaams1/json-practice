# JSON Practice 📘

This project provides hands-on practice with handling JSON files using Python. It includes exercises that simulate real-world data manipulation tasks such as managing book records, student competition data, and a mini movie database.

## 📁 Project Structure

The project is divided into two main exercises:

### Exercise 1: Basic JSON Practice - Book Manager

Manage a list of books stored in a `books.json` file.

#### Tasks:

- Load data from the JSON file.
- Print each book's title and its average rating.
- Add a new book with:
  - Auto-generated ID (next available number).
  - Duplication check by title (case-insensitive).
- Save the updated list back to the file.
- 🔥 **Bonus**: Add a `category` field based on keywords in the title:
  - `"Python"` → `Programming`
  - `"JavaScript"` → `Web Development`
  - Other → `Other`

---

### Exercise 2: Challenging JSON Practice

#### Challenge 1: Students' Championship 🏆

Manage student competition data in a `students.json` file.

##### Tasks:

- Load data from the file.
- Calculate average scores for each student.
- Identify the winner (highest average score).
- Add a `status` field: `"Winner"` or `"Participant"`.
- Add new students with auto-generated IDs (prevent name duplication).
- Save all changes.
- 🔥 **Extra**: Create and print a sorted leaderboard by average score.

#### Challenge 2: Mini Movie Database 🎬

Manage movie records in a `movies.json` file.

##### Tasks:

- Load existing data.
- Search for a movie by title (case-insensitive).
- Add new movies with unique IDs (prevent duplicate titles).
- Update ratings.
- Save changes.
- 🔥 **Bonus**:
  - Generate a report of top 3 movies by rating.
  - Count and print the number of movies per genre.

---

## 🛠 Requirements

- Python 3.x
- No external libraries required (uses built-in `json` module)

## 🚀 How to Run

1. Clone or download the project files.
2. Run the corresponding Python scripts for each exercise.
   ```bash
   python book_manager.py
   python students_championship.py
   python mini_movie_database.py
   ```
3. Follow the prompts or view printed outputs in the terminal.

---

## 📌 Notes

- All data is stored in JSON format and updated in place.
- Make sure your `.json` files are in the correct format before running scripts.
- The project is ideal for beginner to intermediate Python learners.

## 📄 License

This project is for educational use only.
