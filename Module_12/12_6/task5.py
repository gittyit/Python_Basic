import random

def get_element_name(element):
  element_description = ""
  if element == 1:
    element_description = "Камень"
  elif element == 2:
    element_description = "Ножницы"
  elif element == 3:
    element_description = "Бумага"
  return element_description

def calculate_winner(element, pc_element):
  result = ""
  if element == pc_element:
    result = "Ничья."
  
  # 1. Камень бьёт ножницы
  elif element == 1 and pc_element == 2:
   result = "Вы выйграли."
  # 1. Камень бьёт ножницы
  elif element == 2 and pc_element == 1:
   result = "Вы проиграли."
  
  # 2. бумага кроет камень
  elif element == 1 and pc_element == 3:
    result = "Вы проиграли."
  # 2. бумага кроет камень
  elif element == 3 and pc_element == 1:
   result = "Вы выйграли."

  # 3. ножницы режут бумагу
  elif element == 2 and pc_element == 3:
    result = "Вы выйграли."
  # 3. ножницы режут бумагу
  elif element == 3 and pc_element == 2:
    result = "Вы проиграли."
  return result

def rock_paper_scissors():
  print("\nИгра «Камень, ножницы, бумага». Ваш ход.")
  print("1 - Камень")
  print("2 - Ножницы")
  print("3 - Бумага")
  element = int(input("Введите номер предмета: "))
  element_description = get_element_name(element)
  pc_element = random.randint(1, 3)
  print()

  pc_element_description = get_element_name(pc_element)
  
  game_result = calculate_winner(element, pc_element)
  print(game_result)
  
  print(f"\nВыбранный вами предмет: {element_description}")
  print(f"Выбранный компьютером предмет: {pc_element_description}\n")


def guess_the_number():
  number = 0
  number_to_guess = random.randint(1, 10)
  while True:
    print("\nИгра «Угадай число».")
    number = int(input("Введите число: "))
    if number != number_to_guess:
      print("\nВы не угадали.")
      print(f"Введенное число {number}")
    else:
      print(f"\nВы угадали. Загаданное число {number_to_guess}\n")
      break;

def main_menu():
  print("Главное меню:")
  print("1 - «Камень, ножницы, бумага»")
  print("2 - «Угадай число»")
  game_num = int(input("Введите номер игры: "))
  if game_num  == 1:
    rock_paper_scissors()
  elif game_num  == 2:
    guess_the_number()


main_menu()