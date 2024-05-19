import random

words = []

with open('words.txt', 'r', encoding='utf-8') as file_words:
    for row in file_words:
        words.append(row)

print(*words, sep='\n')
print(len(words))
how_many_words = random.randint(55, 72)
with open('result.txt', 'w') as f:
    to_result = []
    for i in range(0, how_many_words):
        word_index = random.randint(0, len(words)-1)
        word = words[word_index]
        to_result.append(word)
        words.pop(word_index)
    to_result.sort()
    first_letter = ""
    for item in to_result:
        if (item[0] != first_letter):
            first_letter = item[0]
            f.write("\n \\textbf{" + first_letter + "} \n")
        f.write("\item {" + item[:-2] + '"---}\n')
        first_letter = item[0].upper()
