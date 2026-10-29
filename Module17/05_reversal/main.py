
text_string = input("Введите строку: ")

h_lpos = text_string.find('h')
h_rpos = text_string.rfind('h')

result_string = text_string[h_lpos+1:h_rpos] if (h_rpos - h_lpos) > 1 else ""
result_string = result_string[::-1]

print(f"Развёрнутая последовательность между первым и последним h: {result_string}")

