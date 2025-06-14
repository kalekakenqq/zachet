try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
        words = content.split()
        print(f"количество слов в файле: {len(words)}")
except FileNotFoundError:
    print("Файл не найден")