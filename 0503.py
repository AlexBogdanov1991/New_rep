import itertools

def create_deck():
    suits = ['❤️', '♦️', '♣️', '♠️']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank} {suit}" for suit in suits for rank in ranks]
    return deck

def generate_permutations(deck, n):
    return list(itertools.permutations(deck[:n]))  # Генерируем перестановки для первых n карт

def save_permutations_to_file(permutations, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for perm in permutations:
            file.write(', '.join(perm) + '\n')

def main():
    deck = create_deck()
    n = int(input("Введите количество карт для перестановок (от 1 до 52): "))

    if n < 1 or n > 52:
        print("Ошибка: количество карт должно быть от 1 до 52.")
        return

    permutations = generate_permutations(deck, n)

    for perm in permutations:
        print(perm)

    save_to_file = input("Хотите сохранить перестановки в файл? (да/нет): ").strip().lower()
    if save_to_file == 'да':
        filename = input("Введите имя файла (например, permutations.txt): ")
        save_permutations_to_file(permutations, filename)
        print(f"Перестановки успешно сохранены в файл {filename}.")

if __name__ == "__main__":
    main()

