with open("resource/words.txt", "r", encoding="utf-8") as file:
    words = file.read().splitlines()

alphabetical = sorted(words)

by_length = sorted(words, key=len)

reverse_order = sorted(words, reverse=True)

with open("sorted_alphabetically.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(alphabetical))

with open("sorted_by_length.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(by_length))

with open("sorted_reverse.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(reverse_order))

print("Сортировка завершена")