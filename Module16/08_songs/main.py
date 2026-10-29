violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_duration_minutes = 0.0

song_list = []
duration_list = []
for song_index in violator_songs:
    song_list.append(song_index[0])
    duration_list.append(song_index[1])


number_of_songs = int(input("Сколько песен выбрать? "))

song_index = 1
while song_index <= number_of_songs:
    song_title = input(f"Название {song_index}-й песни: ")
    if song_list.count(song_title) > 0:
        found_song_list_index = song_list.index(song_title)
        found_song_duration = duration_list[found_song_list_index]
        songs_duration_minutes += found_song_duration
    song_index += 1

songs_duration_minutes = round(songs_duration_minutes, ndigits=2)

print()
print(f"Общее время звучания песен: {songs_duration_minutes} минуты")
