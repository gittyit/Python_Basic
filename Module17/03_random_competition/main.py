from random import randrange

first_team = [randrange(5*100, 10*100)/100 for x in range(21)]
second_team = [randrange(5*100, 10*100)/100 for x in range(21)]

winners = [first_team[x] if first_team[x] > second_team[x] else second_team[x] for x in range(21)]

print(f"Первая команда: {first_team}")
print(f"Вторая команда: {second_team}")
print(f"Победители тура: {winners}")

