violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_play_time = 0

songs_number = int(input("Сколько песен выбрать? "))


song_counter = 0
while song_counter < songs_number :
    song_counter += 1
    
    song_counter_text = ""

    if song_counter == 1:
        song_counter_text = "первой"
    elif song_counter == 2:
        song_counter_text = "второй"
    elif song_counter == 3:
        song_counter_text = "третьей"
    elif song_counter == 4:
        song_counter_text = "четвертой"
    elif song_counter == 5:
        song_counter_text = "пятой"
    elif song_counter == 6:
        song_counter_text = "шестой"
    elif song_counter == 7:
        song_counter_text = "седьмой"
    elif song_counter == 8:
        song_counter_text = "восьмой"
    elif song_counter == 9:
        song_counter_text = "девятой"
    elif song_counter == 10:
        song_counter_text = "десятой"

    song_title = input(f"Название {song_counter_text} песни: ")
    song_time = violator_songs[song_title]
    
    total_play_time += song_time

print()
print("Общее время звучания песен: {:.2f} минуты".format(total_play_time))
