word = input("Введите слово для поиска: ")

count = 0
line_numbers = []

with open("resource/text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    coincident = line.split()
    if word in coincident:
        count += word.count(word)
        line_numbers.append(i)

with open("search_results.txt", "w", encoding="utf-8") as file:
    if count > 0:
        file.write(f"Слово найдено\n")
        file.write(f"Количество: {count}\n")
        file.write(f"Строки: {line_numbers}\n")
    else:
        file.write("Слово не найдено\n")

if count > 0:
    print("Слово найдено")
    print("Количество:", count)
    print("Строки:", line_numbers)
else:
    print("Слово не найдено")