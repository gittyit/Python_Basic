nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result_list = [level3 for level1 in nice_list for level2 in level1 for level3 in level2]

print(result_list)
