

def is_palindrome(word):
    word_len = len(word)
    index_right = word_len
    index_left = 0


    while True:
        char_left = word[index_left]
        char_right = word[index_right-1]


        if char_left != char_right:
            print(f"Слово не является палиндромом")
            return

        if index_right == index_left or index_right - index_left == 1:
            print(f"Слово является палиндромом")
            return
        
        index_left += 1
        index_right -= 1


# Варианты:
# qweewq    (index_right - index_left) == 1 and len % 2 = 0
# racecar   index_right == index_left and len % 2 != 0

print()
word = input("Введите слово: ")
print()

is_palindrome(word)

