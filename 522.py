import os
import shutil

dir_name = "Управление_файлами"
os.makedirs(dir_name, exist_ok=True)

file1_path = os.path.join(dir_name, "file1.txt")
file2_path = os.path.join(dir_name, "file2.txt")

with open(file1_path, 'w', encoding='utf-8') as file1:
    file1.write("Это содержимое file1.")

with open(file2_path, 'w', encoding='utf-8') as file2:
    file2.write("Это содержимое file2.")

print("Содержимое директории:")
for item in os.listdir(dir_name):
    print(item)

os.remove(file2_path)

subdir_name = os.path.join(dir_name, "Поддиректория")
os.makedirs(subdir_name, exist_ok=True)

new_file_path = os.path.join(subdir_name, "file1.txt")
os.rename(file1_path, new_file_path)

shutil.rmtree(dir_name)

print("Все операции выполнены успешно.")

