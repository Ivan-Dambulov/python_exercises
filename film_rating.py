number_of_movies = int(input())
max_rating =  float('-inf')

for i in range(number_of_movies):
    name_of_movie = input()
    rating = float(input())

    if rating > max_rating:
        max_rating += rating


