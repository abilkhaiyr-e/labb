def average_imdb_score(movies):
    total_score = sum(movie['imdb'] for movie in movies)
    num_movies = len(movies)
    if num_movies == 0:
        return 0  # Return 0 if the list is empty to avoid division by zero
    return total_score / num_movies

# Example usage:
# Assuming `movies` is the list of movies provided in the task
avg_score = average_imdb_score(movies)
print("Average IMDB score:", avg_score)
