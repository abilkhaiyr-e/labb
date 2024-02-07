def above_5_5_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]


above_5_5 = above_5_5_movies(movies)
print("Movies with an IMDB score above 5.5:")
for movie in above_5_5:
    print(movie)
