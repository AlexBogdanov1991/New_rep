import itertools


def create_deck():
    suits = ['Черви', 'Бубны', 'Трефы', 'Пики']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank} {suit}" for suit in suits for rank in ranks]
    return deck


def generate_combinations(deck, n):
    return list(itertools.combinations(deck, n))


def save_combinations_to_file(combinations, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for combo in combinations:
            file.write(', '.join(combo) + '\n')


def main():
    deck = create_deck()
    n = int(input("Введите количество карт для комбинаций (от 1 до 52): "))

    if n < 1 or n > 52:
        print("Ошибка: количество карт должно быть от 1 до 52.")
        return

    combinations = generate_combinations(deck, n)


    for combo in combinations:
        print(combo)


    save_to_file = input("Хотите сохранить комбинации в файл? (да/нет): ").strip().lower()
    if save_to_file == 'да':
        filename = input("Введите имя файла (например, combinations.txt): ")
        save_combinations_to_file(combinations, filename)
        print(f"Комбинации успешно сохранены в файл {filename}.")


if __name__ == "__main__":
    main()
