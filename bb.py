import csv

with open('prices.txt', 'r', encoding='utf-8') as infile:
    with open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for line in infile:
            columns = line.strip().split('\t')
            writer.writerow(columns)



import csv

total_cost = 0

with open('prices.csv', 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    for row in reader:
        quantity = int(row[1])
        price_per_item = int(row[2])
        total_cost += quantity * price_per_item

print(f'Общая стоимость заказа: {total_cost} рублей')
