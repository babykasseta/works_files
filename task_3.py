with open("combined.txt", "w", encoding="utf-8") as result:

    with open("resource/file1.txt", "r", encoding="utf-8") as file1:
        result.write("=== Содержимое file1.txt ===\n")
        result.write(file1.read())
        result.write("\n\n")

    with open("resource/file2.txt", "r", encoding="utf-8") as file2:
        result.write("=== Содержимое file2.txt ===\n")
        result.write(file2.read())
        result.write("\n\n")

    with open("resource/file3.txt", "r", encoding="utf-8") as file3:
        result.write("=== Содержимое file3.txt ===\n")
        result.write(file3.read())
        result.write("\n")

print("Файлы объединены в combined.txt")