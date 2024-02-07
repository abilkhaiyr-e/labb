def average_imdb_score_by_category(category, movies):
    category_movies = [movie for movie in movies if movie['category'] == category]
    total_score = sum(movie['imdb'] for movie in category_movies)
    num_movies = len(category_movies)
    if num_movies == 0:
        return 0  # Return 0 if there are no movies under the specified category to avoid division by zero
    return total_score / num_movies

# Example usage:
# Assuming `movies` is the list of movies provided in the task
category_name = input("Enter a category name: ")
avg_score = average_imdb_score_by_category(category_name, movies)
if avg_score:
    print(f"Average IMDB score for movies in the category '{category_name}':", avg_score)
else:
    print(f"No movies found under the category '{category_name}'.")
