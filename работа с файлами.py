import re
from collections import Counter


def get_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        text = re.sub(r'[^\w\s]', '', text).lower()

        words = text.split()
    return words


def get_words_dict(words):
    words_dict = Counter(words)
    return words_dict


def main():
    filename = input("Введите название файла: ").strip()

    words = get_words(filename)

    words_dict = get_words_dict(words)


    print(f"\nКол-во слов: {len(words)}")
    print(f"Кол-во уникальных слов: {len(words_dict)}")
    print("\nВсе использованные слова:")

    for word, count in words_dict.items():
        print(f"{word} {count}")


if __name__ == "__main__":
    main()

