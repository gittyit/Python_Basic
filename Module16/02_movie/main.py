films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_movies_list = []


number_of_favorite_movies = int(input("Сколько фильмов хотите добавить? "))

while number_of_favorite_movies != 0:    
    movie_title = input("Введите название фильма: ")
    
    if movie_title in films:
        if movie_title not in favorite_movies_list:
            favorite_movies_list.append(movie_title)
    else:
        print(f"Ошибка: фильма {movie_title} у нас нет :(")
    number_of_favorite_movies -= 1

favorite_movies = ""
for movie_title in favorite_movies_list:
    favorite_movies += movie_title + ', '

print()
print(f"Ваш список любимых фильмов: {favorite_movies}\n")
