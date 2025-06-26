shopping_list = input("Is milk on the list: ").lower()

print(shopping_list)

if "milk" in shopping_list:
    print("Milk is on the shopping list")
else:
    print("Milk is missing")

movie_titles = ["rocky", "warstars", "batman"]

print("Add a new movie title")
new_movie = input(" > ")

if new_movie not in movie_titles:
    movie_titles.append(new_movie)
else:
    print(f"The movie {new_movie} is already on the list")

print(movie_titles)