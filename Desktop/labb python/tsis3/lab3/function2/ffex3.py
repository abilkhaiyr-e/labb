def movies_by_category(category_name, movies):
    return [movie for movie in movies if movie['category'] == category_name]


category_name = input("Enter a category name: ")
category_movies = movies_by_category(category_name, movies)
if category_movies:
    print(f"Movies under the category '{category_name}':")
    for movie in category_movies:
        print(movie)
else:
    print(f"No movies found under the category '{category_name}'.")
